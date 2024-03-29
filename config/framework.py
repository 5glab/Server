from subprocess import call
from platform import system
import sys, socket, imp, platform

class framework:
    def __init__(self, config):
        self.config = config
        self.check_os()
        self.check_module_exist()
        #self.check_client();
        self.clear_console()
        pass

    def check_os(self):
        os = system()
        print "Framework Version : ", self.config.get("version")
        print "Operating System  : ", os
        print "Platform  Release : ", platform.release()
        print "Platform  Version : ", platform.version()
        if sys.version_info[0] > 3:
            exit("Python  Version   : Must be using Python 3")
        print "Python  Version   : ", str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2])

    def check_module_exist(self):
        for module_ in self.config.get("modules"):
            try:
                imp.find_module(module_)
            except ImportError:
                exit("Required Modules  :  Error : Module '"+ module_ +"' Not Found")
        print "Required Modules  : ", "Found "
        pass

    def clear_console(self):
        os = system()
        if os == 'Linux':
            call('clear', shell = True)
        elif os == 'Windows':
            call('cls', shell = True)
        pass

    def check_client(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.config.get("client_ip"), self.config.get("client_port"))
        try:
            sock.connect(server_address)
            print "Client Status     :  Connect"
        except Exception as e:
            exit("Client Status     :  Disconnect -> %s" %e)
        finally:
            sock.close()
        pass