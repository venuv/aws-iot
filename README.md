# aws-iot-python
Experiments with the [Python AWS IoT SDK](https://github.com/aws/aws-iot-device-sdk-python), and [Boto3](https://boto3.readthedocs.io/en/latest/) which spans AWS and AWS IoT, and bridges between the two.

* jbActivate.py - tests Python IoT SDK to use  MQTT to update a device shadow. Invoked as
>_python jb_activate.py -e \<endpoint\> -r \<rootCAFilePath\> -c \<certFilePath\> -k \<privateKeyFilePath\> -i \<thingId\> -s \<desiredThingState\>_

* active_registry.py - tests a Boto3 script (that can then be used as Lambdas, and behind an API gateway) to invoke IoT operations by publishing to 'system' topics (preceded by a $ sign, such as $aws/things/jio2/shadow/update) that perform REST operations on shadows

* [Chalice](https://github.com/awslabs/chalice) - tests microframework that layers over API GW and Lambda. Auto-packages code as a lambda function and creates REST interfaces. Not tested - auto-creation of language specific SDKs (Android, iOS) beyond REST.

* thingActivation - a Chalice based Lambda function that can be used by web/native apps (e.g. an 'Activation Map' rendering) to query a DynamoDB table of activations. The Lambda function assumes that a DynamoDB table named 'Activations' with schema [thingId, Duration, Latitude, Longitude, Time] exists