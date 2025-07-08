// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtlebot_cosmo_interface:srv/MoveitControl.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__BUILDER_HPP_
#define TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtlebot_cosmo_interface/srv/detail/moveit_control__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtlebot_cosmo_interface
{

namespace srv
{

namespace builder
{

class Init_MoveitControl_Request_waypoints
{
public:
  explicit Init_MoveitControl_Request_waypoints(::turtlebot_cosmo_interface::srv::MoveitControl_Request & msg)
  : msg_(msg)
  {}
  ::turtlebot_cosmo_interface::srv::MoveitControl_Request waypoints(::turtlebot_cosmo_interface::srv::MoveitControl_Request::_waypoints_type arg)
  {
    msg_.waypoints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_cosmo_interface::srv::MoveitControl_Request msg_;
};

class Init_MoveitControl_Request_posename
{
public:
  explicit Init_MoveitControl_Request_posename(::turtlebot_cosmo_interface::srv::MoveitControl_Request & msg)
  : msg_(msg)
  {}
  Init_MoveitControl_Request_waypoints posename(::turtlebot_cosmo_interface::srv::MoveitControl_Request::_posename_type arg)
  {
    msg_.posename = std::move(arg);
    return Init_MoveitControl_Request_waypoints(msg_);
  }

private:
  ::turtlebot_cosmo_interface::srv::MoveitControl_Request msg_;
};

class Init_MoveitControl_Request_cmd
{
public:
  Init_MoveitControl_Request_cmd()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveitControl_Request_posename cmd(::turtlebot_cosmo_interface::srv::MoveitControl_Request::_cmd_type arg)
  {
    msg_.cmd = std::move(arg);
    return Init_MoveitControl_Request_posename(msg_);
  }

private:
  ::turtlebot_cosmo_interface::srv::MoveitControl_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_cosmo_interface::srv::MoveitControl_Request>()
{
  return turtlebot_cosmo_interface::srv::builder::Init_MoveitControl_Request_cmd();
}

}  // namespace turtlebot_cosmo_interface


namespace turtlebot_cosmo_interface
{

namespace srv
{

namespace builder
{

class Init_MoveitControl_Response_response
{
public:
  Init_MoveitControl_Response_response()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtlebot_cosmo_interface::srv::MoveitControl_Response response(::turtlebot_cosmo_interface::srv::MoveitControl_Response::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_cosmo_interface::srv::MoveitControl_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_cosmo_interface::srv::MoveitControl_Response>()
{
  return turtlebot_cosmo_interface::srv::builder::Init_MoveitControl_Response_response();
}

}  // namespace turtlebot_cosmo_interface

#endif  // TURTLEBOT_COSMO_INTERFACE__SRV__DETAIL__MOVEIT_CONTROL__BUILDER_HPP_
