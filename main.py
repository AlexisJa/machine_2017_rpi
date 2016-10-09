import cameracontrol
import drivercommunication
import pololucontrol
import stmcontrol

def wait_for_instructions():
    pass
    # should be via the DriverCommunication class


if __name__ == '__main__':

    camera_control = cameracontrol.CameraControl(server = '127.0.0.1')
    #setup GPIO, SPI
    
    while True:
        print('waiting')
        wait_for_instructions()


