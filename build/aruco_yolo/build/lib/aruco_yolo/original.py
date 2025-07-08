import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage, CameraInfo
from cv_bridge import CvBridge
import cv2
import numpy as np

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        
        self.bridge = CvBridge()
        
        # Declare parameter with default integer value
        self.video_port = self.declare_parameter('video_port', 0).get_parameter_value().integer_value

        self.get_logger().info(f'Get...... video_port parameter : {self.video_port}')

        # image_raw 이미지 퍼블리셔 생성
        self.image_raw_publisher_ = self.create_publisher(Image, 'image_raw', 10)
        self.image_publisher_ = self.create_publisher(Image, 'image', 10)
        # jpeg corped 이미지 퍼블리셔 생성
        self.publisher_ = self.create_publisher(CompressedImage, 'image_croped_raw/compressed', 10)
        # jped full 이미지 퍼블리셔 생성
        self.compressed_publisher_ = self.create_publisher(CompressedImage, 'image_raw/compressed', 10)

        # ── 화이트 밸런스 객체 (SimpleWB) ─────────────────────────────
        try:
            self.simple_wb = cv2.xphoto.createSimpleWB()
            self.simple_wb.setP(0.5)          # WB 강도 0.0~1.0
        except AttributeError:                # xphoto 미포함 빌드 대비
            self.simple_wb = None

        # ── CLAHE 객체 (적응형 히스토그램 평활화) ────────────────────
        self.clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

        # ── (선택) 보정 결과용 퍼블리셔 ─────────────────────────────
        self.image_lane_pub_ = self.create_publisher(Image, 'image_lane_preproc', 10)

        # 주기적인 이미지 전송을 위한 타이머 설정 (주기: 1초)
        self.timer = self.create_timer(0.2, self.publish_image)
        # OpenCV 비디오 캡처 객체 생성 (카메라 0번 장치 사용)
        self.cap = cv2.VideoCapture(self.video_port)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

        # 카메라에서 한 프레임 읽기
        ret, frame = self.cap.read()

        # Get raw image size (before compression)
        height, width = frame.shape[:2]
        self.get_logger().info(f'Raw frame size: width={width}, height={height}')

        if ret:
            self.get_logger().info(f"Frame type:, {type(frame)}")
            self.get_logger().info(f"Shape (Height, Width, Channels):, {frame.shape}")
            self.get_logger().info(f"Height:, {frame.shape[0]}")
            self.get_logger().info(f"Width:, {frame.shape[1]}")
            self.get_logger().info(f"Channels:, {frame.shape[2]}")  # Usually 3 for BGR
            self.get_logger().info(f"Data type:, {frame.dtype}")

            #대부분의 카메라 드라이버는 /camera_info 토픽으로 캘리브레이션 데이터를 발행합니다:
            self.info_pub = self.create_publisher(CameraInfo, '/camera/camera_info', 10)

            # Set dummy camera parameters
            self.camera_info = CameraInfo()
            self.camera_info.width = 320
            self.camera_info.height = 240
            self.camera_info.k = [525.0, 0.0, 320.0,
                                0.0, 525.0, 240.0,
                                0.0, 0.0, 1.0]  # dummy intrinsic matrix
            self.camera_info.d = [0.0, 0.0, 0.0, 0.0, 0.0]
            self.camera_info.r = [1.0, 0.0, 0.0,
                                0.0, 1.0, 0.0,
                                0.0, 0.0, 1.0]
            self.camera_info.p = [525.0, 0.0, 320.0, 0.0,
                                0.0, 525.0, 240.0, 0.0,
                                0.0, 0.0, 525.0, 0.0]
            self.camera_info.distortion_model = 'plumb_bob'

    def publish_image(self):
        # 카메라에서 한 프레임 읽기
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error('Video Pen Error!...')
            return

        orig = frame.copy()                       # ③ 채도 복원용
        # ===== 1) ROI(하단 1/3) 채도 평균으로 파라미터 자동조절 =========
        h = frame.shape[0]
        hsv_roi = cv2.cvtColor(frame[int(h*2/3):], cv2.COLOR_BGR2HSV)
        s_mean = hsv_roi[:, :, 1].mean()
        if s_mean > 30:              # 노란선이 매우 가까움
            if self.simple_wb is not None:
                self.simple_wb.setP(0.15)
            self.clahe.setClipLimit(1.0)
            beta = 0
        else:                        # 평상시
            if self.simple_wb is not None:
                self.simple_wb.setP(0.5)
            self.clahe.setClipLimit(2.0)
            beta = -20

        # ===== 2) 화이트 밸런스 =========================================
        frame = (self.simple_wb.balanceWhite(frame)
                 if self.simple_wb else self.grayworld_wb(frame))

        # ===== 3) LAB → L-CLAHE ========================================
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        l = self.clahe.apply(l)
        frame = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)

        # ===== 4) 선형 밝기 보정(가변 β) ================================
        frame = cv2.convertScaleAbs(frame, alpha=1.0, beta=beta)

        # ===== 5) 노란선 채도 복원 =====================================
        hsv_proc = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_orig = cv2.cvtColor(orig,  cv2.COLOR_BGR2HSV)
        yellow = cv2.inRange(hsv_orig, (15,40,50), (35,255,255))
        hsv_proc[:,:,1] = np.where(yellow>0, hsv_orig[:,:,1], hsv_proc[:,:,1])
        hsv_proc[:,:,2] = np.where(yellow>0, hsv_orig[:,:,2], hsv_proc[:,:,2])
        frame = cv2.cvtColor(hsv_proc, cv2.COLOR_HSV2BGR)

        # ── 4) (옵션) 보정 결과 토픽 추가 퍼블리시 ───────────────
        lane_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        lane_msg.header.stamp = self.get_clock().now().to_msg()
        lane_msg.header.frame_id = 'camera_frame'
        self.image_lane_pub_.publish(lane_msg)
        
        if ret:
            ########## 1. Raw Image, Convert OpenCV image (numpy) to ROS Image message
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            now = self.get_clock().now().to_msg()
            msg.header.stamp = now
            msg.header.frame_id = 'camera_frame'
            self.image_raw_publisher_.publish(msg)
            #self.get_logger().info('Published image to /image_raw')
            ############## camera/image_raw topic publish
            self.image_publisher_.publish(msg)
            #### camera_info topic publish
            self.camera_info.header.stamp = now
            self.camera_info.header.frame_id = 'camera_frame'
            self.info_pub.publish(self.camera_info)

            ######### 2. Compressed Image, with some Rectanges
            height, width, _ = frame.shape
            rect_w, rect_h = 300, 300
            x1 = (width - rect_w) // 2
            y1 = (height - rect_h) // 2
            x2 = x1 + rect_w
            y2 = y1 + rect_h

            top_left = (x1, y1)
            bottom_right = (x2, y2)
            color = (200, 100,100)  # Green
            thickness = 3        # Outline only
            
            # Draw ROI rectangle: from (50, 0) to (1250, 720)
            top_left = (50,720-50)
            bottom_right = (50,1280-50)
            color = (0, 255, 0)  # Green
            thickness = 2        # Outline only

             # OpenCV 이미지 (BGR)을 JPEG로 압축
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 30]  # 90은 압축 품질
            _, compressed_image = cv2.imencode('.jpg', frame, encode_param)

            # 압축된 이미지를 CompressedImage 메시지로 변환
            msg = CompressedImage()
            msg.header.stamp = self.get_clock().now().to_msg()  # 타임스탬프 추가
            msg.header.frame_id = "camera"  # 프레임 ID 설정
            msg.format = "jpeg"  # 압축 형식 설정
            msg.data = compressed_image.tobytes()  # 압축된 이미지 데이터

            # CompressedImage 퍼블리시
            self.compressed_publisher_.publish(msg)
        else:
            self.get_logger().error('Video Pen Error!...')

    def grayworld_wb(self, img: np.ndarray) -> np.ndarray:
        b_avg, g_avg, r_avg = img.mean(axis=(0, 1))
        k = (r_avg + g_avg + b_avg) / 3.0
        kb, kg, kr = k / b_avg, k / g_avg, k / r_avg
        img = img.astype(np.float32)
        img[:, :, 0] = np.clip(img[:, :, 0] * kb, 0, 255)
        img[:, :, 1] = np.clip(img[:, :, 1] * kg, 0, 255)
        img[:, :, 2] = np.clip(img[:, :, 2] * kr, 0, 255)
        return img.astype(np.uint8)

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    
    # ROS 2 노드 실행
    rclpy.spin(image_publisher)

    # 종료 시 리소스 해제
    image_publisher.cap.release()
    rclpy.shutdown()

if __name__ == '__main__':
    main()