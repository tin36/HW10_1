# "принцесса устала и прилегла поспать"
# "принцесса прячется"
# "принцесса прогуливается туда-сюда"

class Princess:
    def sleep(self):
        print('принцесса устала и прилегла поспать')

    def hide(self):
        print('принцесса прячется')

    def walk(self):
        print('принцесса прогуливается туда-сюда')


leia = Princess()
leia.hide()
leia.sleep()
leia.walk()