#include <iostream>
#include <memory>

#include "ros/ros.h"
#include "simple_tf_buffer_server/buffer_server.h"

#include "boost/program_options.hpp"

namespace po = boost::program_options;

int main(int argc, char** argv) {
  int num_threads = 0;

  po::options_description desc("Options");
  // clang-format off
  desc.add_options()
    ("help", "show usage")
    ("num_threads", po::value<int>(&num_threads)->default_value(10),
     "Number of handler threads. 0 means number of CPU cores.")
  ;
  // clang-format on
  po::variables_map vm;
  po::store(po::parse_command_line(argc, argv, desc), vm);
  po::notify(vm);
  if (vm.count("help")) {
    std::cout << desc << std::endl;
    return EXIT_FAILURE;
  }

  ros::init(argc, argv, "simple_tf_buffer_server");
  auto private_node_handle = std::make_shared<ros::NodeHandle>("~");

  ROS_INFO_STREAM("Starting server with " << num_threads << " handler threads");
  tf2_ros::SimpleBufferServer server(private_node_handle);
  auto FLAGS_num_threads = 10;
  ros::AsyncSpinner spinner(FLAGS_num_threads);
  spinner.start();
  ros::waitForShutdown();
  spinner.stop();

  return EXIT_SUCCESS;
}