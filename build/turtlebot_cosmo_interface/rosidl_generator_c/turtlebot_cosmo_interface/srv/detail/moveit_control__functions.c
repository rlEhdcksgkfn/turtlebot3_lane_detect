// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from turtlebot_cosmo_interface:srv/MoveitControl.idl
// generated code does not contain a copyright notice
#include "turtlebot_cosmo_interface/srv/detail/moveit_control__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `posename`
#include "rosidl_runtime_c/string_functions.h"
// Member `waypoints`
#include "geometry_msgs/msg/detail/pose_array__functions.h"

bool
turtlebot_cosmo_interface__srv__MoveitControl_Request__init(turtlebot_cosmo_interface__srv__MoveitControl_Request * msg)
{
  if (!msg) {
    return false;
  }
  // cmd
  // posename
  if (!rosidl_runtime_c__String__init(&msg->posename)) {
    turtlebot_cosmo_interface__srv__MoveitControl_Request__fini(msg);
    return false;
  }
  // waypoints
  if (!geometry_msgs__msg__PoseArray__init(&msg->waypoints)) {
    turtlebot_cosmo_interface__srv__MoveitControl_Request__fini(msg);
    return false;
  }
  return true;
}

void
turtlebot_cosmo_interface__srv__MoveitControl_Request__fini(turtlebot_cosmo_interface__srv__MoveitControl_Request * msg)
{
  if (!msg) {
    return;
  }
  // cmd
  // posename
  rosidl_runtime_c__String__fini(&msg->posename);
  // waypoints
  geometry_msgs__msg__PoseArray__fini(&msg->waypoints);
}

bool
turtlebot_cosmo_interface__srv__MoveitControl_Request__are_equal(const turtlebot_cosmo_interface__srv__MoveitControl_Request * lhs, const turtlebot_cosmo_interface__srv__MoveitControl_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // cmd
  if (lhs->cmd != rhs->cmd) {
    return false;
  }
  // posename
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->posename), &(rhs->posename)))
  {
    return false;
  }
  // waypoints
  if (!geometry_msgs__msg__PoseArray__are_equal(
      &(lhs->waypoints), &(rhs->waypoints)))
  {
    return false;
  }
  return true;
}

bool
turtlebot_cosmo_interface__srv__MoveitControl_Request__copy(
  const turtlebot_cosmo_interface__srv__MoveitControl_Request * input,
  turtlebot_cosmo_interface__srv__MoveitControl_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // cmd
  output->cmd = input->cmd;
  // posename
  if (!rosidl_runtime_c__String__copy(
      &(input->posename), &(output->posename)))
  {
    return false;
  }
  // waypoints
  if (!geometry_msgs__msg__PoseArray__copy(
      &(input->waypoints), &(output->waypoints)))
  {
    return false;
  }
  return true;
}

turtlebot_cosmo_interface__srv__MoveitControl_Request *
turtlebot_cosmo_interface__srv__MoveitControl_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlebot_cosmo_interface__srv__MoveitControl_Request * msg = (turtlebot_cosmo_interface__srv__MoveitControl_Request *)allocator.allocate(sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Request));
  bool success = turtlebot_cosmo_interface__srv__MoveitControl_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
turtlebot_cosmo_interface__srv__MoveitControl_Request__destroy(turtlebot_cosmo_interface__srv__MoveitControl_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    turtlebot_cosmo_interface__srv__MoveitControl_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence__init(turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlebot_cosmo_interface__srv__MoveitControl_Request * data = NULL;

  if (size) {
    data = (turtlebot_cosmo_interface__srv__MoveitControl_Request *)allocator.zero_allocate(size, sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = turtlebot_cosmo_interface__srv__MoveitControl_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        turtlebot_cosmo_interface__srv__MoveitControl_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence__fini(turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      turtlebot_cosmo_interface__srv__MoveitControl_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence *
turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence * array = (turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence *)allocator.allocate(sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence__destroy(turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence__are_equal(const turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence * lhs, const turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!turtlebot_cosmo_interface__srv__MoveitControl_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence__copy(
  const turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence * input,
  turtlebot_cosmo_interface__srv__MoveitControl_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    turtlebot_cosmo_interface__srv__MoveitControl_Request * data =
      (turtlebot_cosmo_interface__srv__MoveitControl_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!turtlebot_cosmo_interface__srv__MoveitControl_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          turtlebot_cosmo_interface__srv__MoveitControl_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!turtlebot_cosmo_interface__srv__MoveitControl_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
turtlebot_cosmo_interface__srv__MoveitControl_Response__init(turtlebot_cosmo_interface__srv__MoveitControl_Response * msg)
{
  if (!msg) {
    return false;
  }
  // response
  return true;
}

void
turtlebot_cosmo_interface__srv__MoveitControl_Response__fini(turtlebot_cosmo_interface__srv__MoveitControl_Response * msg)
{
  if (!msg) {
    return;
  }
  // response
}

bool
turtlebot_cosmo_interface__srv__MoveitControl_Response__are_equal(const turtlebot_cosmo_interface__srv__MoveitControl_Response * lhs, const turtlebot_cosmo_interface__srv__MoveitControl_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // response
  if (lhs->response != rhs->response) {
    return false;
  }
  return true;
}

bool
turtlebot_cosmo_interface__srv__MoveitControl_Response__copy(
  const turtlebot_cosmo_interface__srv__MoveitControl_Response * input,
  turtlebot_cosmo_interface__srv__MoveitControl_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // response
  output->response = input->response;
  return true;
}

turtlebot_cosmo_interface__srv__MoveitControl_Response *
turtlebot_cosmo_interface__srv__MoveitControl_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlebot_cosmo_interface__srv__MoveitControl_Response * msg = (turtlebot_cosmo_interface__srv__MoveitControl_Response *)allocator.allocate(sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Response));
  bool success = turtlebot_cosmo_interface__srv__MoveitControl_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
turtlebot_cosmo_interface__srv__MoveitControl_Response__destroy(turtlebot_cosmo_interface__srv__MoveitControl_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    turtlebot_cosmo_interface__srv__MoveitControl_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence__init(turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlebot_cosmo_interface__srv__MoveitControl_Response * data = NULL;

  if (size) {
    data = (turtlebot_cosmo_interface__srv__MoveitControl_Response *)allocator.zero_allocate(size, sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = turtlebot_cosmo_interface__srv__MoveitControl_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        turtlebot_cosmo_interface__srv__MoveitControl_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence__fini(turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      turtlebot_cosmo_interface__srv__MoveitControl_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence *
turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence * array = (turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence *)allocator.allocate(sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence__destroy(turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence__are_equal(const turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence * lhs, const turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!turtlebot_cosmo_interface__srv__MoveitControl_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence__copy(
  const turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence * input,
  turtlebot_cosmo_interface__srv__MoveitControl_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(turtlebot_cosmo_interface__srv__MoveitControl_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    turtlebot_cosmo_interface__srv__MoveitControl_Response * data =
      (turtlebot_cosmo_interface__srv__MoveitControl_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!turtlebot_cosmo_interface__srv__MoveitControl_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          turtlebot_cosmo_interface__srv__MoveitControl_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!turtlebot_cosmo_interface__srv__MoveitControl_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
