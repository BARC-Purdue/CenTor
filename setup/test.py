# import os
# import shutil

# from stem.control import Controller

# print(' * Connecting to tor')

# with Controller.from_port() as controller:
#   controller.authenticate()

#   # All hidden services have a directory on disk. Lets put ours in tor's data
#   # directory.

#   hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', '/tmp'), 'hello_world')

#   # Create a hidden service where visitors of port 80 get redirected to local
#   # port 5000 (this is where Flask runs by default).

#   print(" * Creating our hidden service in %s" % hidden_service_dir)
#   result = controller.create_hidden_service(hidden_service_dir, 80, target_port = 80)
#   print(result)
#   # The hostname is only available when we can read the hidden service
#   # directory. This requires us to be running with the same user as tor.

#   if result.hostname:
#     print(" * Our service is available at %s, press ctrl+c to quit")
#   else:
#     print(" * Unable to determine our service's hostname, probably due to being unable to read the hidden service directory")

#   try:
#     enter = input("Press to exit")
#   finally:
#     # Shut down the hidden service and clean it off disk. Note that you *don't*
#     # want to delete the hidden service directory if you'd like to have this
#     # same *.onion address in the future.

#     print(" * Shutting down our hidden service")
#     controller.remove_hidden_service(hidden_service_dir)
#     shutil.rmtree(hidden_service_dir)