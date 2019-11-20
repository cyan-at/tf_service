import rospy
# Importing tf2_geometry_msgs to register geometry_msgs
# types with tf2_ros.TransformRegistration
import tf2_geometry_msgs
import tf2_ros
from simple_tf_buffer_server.client import SimpleBufferClientBinding


class SimpleBufferClient(tf2_ros.BufferInterface):
    """
    Extends the raw C++ binding to the full Python tf2_ros.BufferInterface.
    The interface is exactly the same as the old action-based client.
    """

    def __init__(self, server_node_name):
        tf2_ros.BufferInterface.__init__(self)
        # All actual work is done by the C++ binding.
        self.client = SimpleBufferClientBinding(server_node_name)

    def wait_for_server(self, timeout=rospy.Duration(-1)):
        """
        Block until the server is ready to respond to requests. 

        :param timeout: Time to wait for the server.
        :return: True if the server is ready, false otherwise.
        :rtype: bool
        """
        return self.client.reconnect(timeout)

    def lookup_transform(self, target_frame, source_frame, time,
                         timeout=rospy.Duration(0.0)):
        """
        Get the transform from the source frame to the target frame.

        :param target_frame: Name of the frame to transform into.
        :param source_frame: Name of the input frame.
        :param time: The time at which to get the transform. (0 will get the latest) 
        :param timeout: (Optional) Time to wait for the target frame to become available.
        :return: The transform between the frames.
        :rtype: :class:`geometry_msgs.msg.TransformStamped`
        """
        return self.client.lookup_transform(target_frame, source_frame, time,
                                            timeout)

    # lookup, advanced api
    def lookup_transform_full(self, target_frame, target_time, source_frame,
                              source_time, fixed_frame,
                              timeout=rospy.Duration(0.0)):
        """
        Get the transform from the source frame to the target frame using the advanced API.

        :param target_frame: Name of the frame to transform into.
        :param target_time: The time to transform to. (0 will get the latest) 
        :param source_frame: Name of the input frame.
        :param source_time: The time at which source_frame will be evaluated. (0 will get the latest) 
        :param fixed_frame: Name of the frame to consider constant in time.
        :param timeout: (Optional) Time to wait for the target frame to become available.
        :return: The transform between the frames.
        :rtype: :class:`geometry_msgs.msg.TransformStamped`
        """
        return self.client.lookup_transform(target_frame, target_time,
                                            source_frame, source_time,
                                            fixed_frame, timeout)

    # can, simple api
    def can_transform(self, target_frame, source_frame, time,
                      timeout=rospy.Duration(0.0)):
        """
        Check if a transform from the source frame to the target frame is possible.

        :param target_frame: Name of the frame to transform into.
        :param source_frame: Name of the input frame.
        :param time: The time at which to get the transform. (0 will get the latest) 
        :param timeout: (Optional) Time to wait for the target frame to become available.
        :param return_debug_type: (Optional) If true, return a tuple representing debug information.
        :return: True if the transform is possible, false otherwise.
        :rtype: bool
        """
        return self.client.can_transform(target_frame, source_frame, time,
                                         timeout, "")

    def can_transform_full(self, target_frame, target_time, source_frame,
                           source_time, fixed_frame,
                           timeout=rospy.Duration(0.0)):
        """
        Check if a transform from the source frame to the target frame is possible (advanced API).

        Must be implemented by a subclass of BufferInterface.

        :param target_frame: Name of the frame to transform into.
        :param target_time: The time to transform to. (0 will get the latest) 
        :param source_frame: Name of the input frame.
        :param source_time: The time at which source_frame will be evaluated. (0 will get the latest) 
        :param fixed_frame: Name of the frame to consider constant in time.
        :param timeout: (Optional) Time to wait for the target frame to become available.
        :param return_debug_type: (Optional) If true, return a tuple representing debug information.
        :return: True if the transform is possible, false otherwise.
        :rtype: bool
        """
        return self.client.can_transform(target_frame, target_time,
                                         source_frame, source_time,
                                         fixed_frame, timeout, "")