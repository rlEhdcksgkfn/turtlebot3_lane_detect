// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from turtlebot_cosmo_interface:srv/MoveitControl.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__TRAITS_HPP_
#define TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "turtlebot_cosmo_interface/srv/detail/moveit_control__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'waypoints'
#include "geometry_msgs/msg/detail/pose_array__traits.hpp"

namespace turtlebot_cosmo_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const MoveitControl_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: cmd
  {
    out << "cmd: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd, out);
    out << ", ";
  }

  // member: posename
  {
    out << "posename: ";
    rosidl_generator_traits::value_to_yaml(msg.posename, out);
    out << ", ";
  }

  // member: waypoints
  {
    out << "waypoints: ";
    to_flow_style_yaml(msg.waypoints, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveitControl_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: cmd
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd, out);
    out << "\n";
  }

  // member: posename
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "posename: ";
    rosidl_generator_traits::value_to_yaml(msg.posename, out);
    out << "\n";
  }

  // member: waypoints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoints:\n";
    to_block_style_yaml(msg.waypoints, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveitControl_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace turtlebot_cosmo_interface

namespace rosidl_generator_traits
{

[[deprecated("use turtlebot_cosmo_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtlebot_cosmo_interface::srv::MoveitControl_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtlebot_cosmo_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtlebot_cosmo_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const turtlebot_cosmo_interface::srv::MoveitControl_Request & msg)
{
  return turtlebot_cosmo_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<turtlebot_cosmo_interface::srv::MoveitControl_Request>()
{
  return "turtlebot_cosmo_interface::srv::MoveitControl_Request";
}

template<>
inline const char * name<turtlebot_cosmo_interface::srv::MoveitControl_Request>()
{
  return "turtlebot_cosmo_interface/srv/MoveitControl_Request";
}

template<>
struct has_fixed_size<turtlebot_cosmo_interface::srv::MoveitControl_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<turtlebot_cosmo_interface::srv::MoveitControl_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<turtlebot_cosmo_interface::srv::MoveitControl_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace turtlebot_cosmo_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const MoveitControl_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: response
  {
    out << "response: ";
    rosidl_generator_traits::value_to_yaml(msg.response, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveitControl_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "response: ";
    rosidl_generator_traits::value_to_yaml(msg.response, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveitControl_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace turtlebot_cosmo_interface

namespace rosidl_generator_traits
{

[[deprecated("use turtlebot_cosmo_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtlebot_cosmo_interface::srv::MoveitControl_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtlebot_cosmo_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtlebot_cosmo_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const turtlebot_cosmo_interface::srv::MoveitControl_Response & msg)
{
  return turtlebot_cosmo_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<turtlebot_cosmo_interface::srv::MoveitControl_Response>()
{
  return "turtlebot_cosmo_interface::srv::MoveitControl_Response";
}

template<>
inline const char * name<turtlebot_cosmo_interface::srv::MoveitControl_Response>()
{
  return "turtlebot_cosmo_interface/srv/MoveitControl_Response";
}

template<>
struct has_fixed_size<turtlebot_cosmo_interface::srv::MoveitControl_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<turtlebot_cosmo_interface::srv::MoveitControl_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<turtlebot_cosmo_interface::srv::MoveitControl_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<turtlebot_cosmo_interface::srv::MoveitControl>()
{
  return "turtlebot_cosmo_interface::srv::MoveitControl";
}

template<>
inline const char * name<turtlebot_cosmo_interface::srv::MoveitControl>()
{
  return "turtlebot_cosmo_interface/srv/MoveitControl";
}

template<>
struct has_fixed_size<turtlebot_cosmo_interface::srv::MoveitControl>
  : std::integral_constant<
    bool,
    has_fixed_size<turtlebot_cosmo_interface::srv::MoveitControl_Request>::value &&
    has_fixed_size<turtlebot_cosmo_interface::srv::MoveitControl_Response>::value
  >
{
};

template<>
struct has_bounded_size<turtlebot_cosmo_interface::srv::MoveitControl>
  : std::integral_constant<
    bool,
    has_bounded_size<turtlebot_cosmo_interface::srv::MoveitControl_Request>::value &&
    has_bounded_size<turtlebot_cosmo_interface::srv::MoveitControl_Response>::value
  >
{
};

template<>
struct is_service<turtlebot_cosmo_interface::srv::MoveitControl>
  : std::true_type
{
};

template<>
struct is_service_request<turtlebot_cosmo_interface::srv::MoveitControl_Request>
  : std::true_type
{
};

template<>
struct is_service_response<turtlebot_cosmo_interface::srv::MoveitControl_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__TRAITS_HPP_
