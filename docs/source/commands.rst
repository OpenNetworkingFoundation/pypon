Pypon module
=============

.. automodule:: pypon
	:members:

Device Info
-----------------------

.. automodule:: pypon.device_info

.. autoclass:: DeviceInfo

	Spawns a new Python Process to execute a gRPC call to Voltha-BBSim using the host and port information provided by the user. The call returns the OLT information (including model, serial number, etc).

	.. automethod:: start()

	.. automethod:: main(host_and_port)

	.. automethod:: get_device_info()

PON Port Info
-------------------------

.. automodule:: pypon.interface_info

.. autoclass:: InterfaceInfo

	Spawns a new Python Process to execute a gRPC call to Voltha-BBSim using the host and port information provided by the user. The call returns the status of the PON interface specified by the user.

	.. automethod:: start()

	.. automethod:: run(intf_id)

	.. automethod:: get_status(if_id)

ONU Info
--------------------

.. automodule:: pypon.onu_info

.. autoclass:: OnuInfo

	Spawns a new Python Process to execute a gRPC call to Voltha-BBSim using the host and port information provided by the user. The call retrieves the status of the desired ONU using the PON port number and ONU ID specified by the user.

	.. automethod:: start()

	.. automethod:: run(intf_id)

	.. automethod:: get_status(if_id)
