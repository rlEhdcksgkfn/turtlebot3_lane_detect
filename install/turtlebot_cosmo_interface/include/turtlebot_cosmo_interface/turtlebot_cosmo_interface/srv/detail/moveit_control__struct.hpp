// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from turtlebot_cosmo_interface:srv/MoveitControl.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__STRUCT_HPP_
#define TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'waypoints'
#include "geometry_msgs/msg/detail/pose_array__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__turtlebot_cosmo_interface__srv__MoveitControl_Request __attribute__((deprecated))
#else
# define DEPRECATED__turtlebot_cosmo_interface__srv__MoveitControl_Request __declspec(deprecated)
#endif

namespace turtlebot_cosmo_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MoveitControl_Request_
{
  using Type = MoveitControl_Request_<ContainerAllocator>;

  explicit MoveitControl_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : waypoints(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cmd = 0l;
      this->posename = "";
    }
  }

  explicit MoveitControl_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : posename(_alloc),
    waypoints(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cmd = 0l;
      this->posename = "";
    }
  }

  // field types and members
  using _cmd_type =
    int32_t;
  _cmd_type cmd;
  using _posename_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _posename_type posename;
  using _waypoints_type =
    geometry_msgs::msg::PoseArray_<ContainerAllocator>;
  _waypoints_type waypoints;

  // setters for named parameter idiom
  Type & set__cmd(
    const int32_t & _arg)
  {
    this->cmd = _arg;
    return *this;
  }
  Type & set__posename(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->posename = _arg;
    return *this;
  }
  Type & set__waypoints(
    const geometry_msgs::msg::PoseArray_<ContainerAllocator> & _arg)
  {
    this->waypoints = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtlebot_cosmo_interface__srv__MoveitControl_Request
    std::shared_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtlebot_cosmo_interface__srv__MoveitControl_Request
    std::shared_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveitControl_Request_ & other) const
  {
    if (this->cmd != other.cmd) {
      return false;
    }
    if (this->posename != other.posename) {
      return false;
    }
    if (this->waypoints != other.waypoints) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveitControl_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveitControl_Request_

// alias to use template instance with default allocator
using MoveitControl_Request =
  turtlebot_cosmo_interface::srv::MoveitControl_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace turtlebot_cosmo_interface


#ifndef _WIN32
# define DEPRECATED__turtlebot_cosmo_interface__srv__MoveitControl_Response __attribute__((deprecated))
#else
# define DEPRECATED__turtlebot_cosmo_interface__srv__MoveitControl_Response __declspec(deprecated)
#endif

namespace turtlebot_cosmo_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MoveitControl_Response_
{
  using Type = MoveitControl_Response_<ContainerAllocator>;

  explicit MoveitControl_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->response = false;
    }
  }

  explicit MoveitControl_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->response = false;
    }
  }

  // field types and members
  using _response_type =
    bool;
  _response_type response;

  // setters for named parameter idiom
  Type & set__response(
    const bool & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtlebot_cosmo_interface__srv__MoveitControl_Response
    std::shared_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtlebot_cosmo_interface__srv__MoveitControl_Response
    std::shared_ptr<turtlebot_cosmo_interface::srv::MoveitControl_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveitControl_Response_ & other) const
  {
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveitControl_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveitControl_Response_

// alias to use template instance with default allocator
using MoveitControl_Response =
  turtlebot_cosmo_interface::srv::MoveitControl_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace turtlebot_cosmo_interface

namespace turtlebot_cosmo_interface
{

namespace srv
{

struct MoveitControl
{
  using Request = turtlebot_cosmo_interface::srv::MoveitControl_Request;
  using Response = turtlebot_cosmo_interface::srv::MoveitControl_Response;
};

}  // namespace srv

}  // namespace turtlebot_cosmo_interface

#endif  // TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__STRUCT_HPP_
