// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from turtlebot_cosmo_interface:srv/MoveitControl.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__STRUCT_H_
#define TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'posename'
#include "rosidl_runtime_c/string.h"
// Member 'waypoints'
#include "geometry_msgs/msg/detail/pose_array__struct.h"

/// Struct defined in srv/MoveitControl in the package turtlebot_cosmo_interface.
typedef struct turtlebot_cosmo_interface__srv__MoveitControl_Request
{
  int32_t cmd;
  rosidl_runtime_c__String posename;
  geometry_msgs__msg__PoseArray waypoints;
} turtlebot_cosmo_interface__srv__MoveitControl_Request;

// Struct for a sequence of turtlebot_cosmo_interface__srv__MoveitControl_Request.
typedef struct turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence
{
  turtlebot_cosmo_interface__srv__MoveitControl_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/MoveitControl in the package turtlebot_cosmo_interface.
typedef struct turtlebot_cosmo_interface__srv__MoveitControl_Response
{
  bool response;
} turtlebot_cosmo_interface__srv__MoveitControl_Response;

// Struct for a sequence of turtlebot_cosmo_interface__srv__MoveitControl_Response.
typedef struct turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence
{
  turtlebot_cosmo_interface__srv__MoveitControl_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__STRUCT_H_
