from time import sleep


class traffic_light:
    color = "Чёрный"

    def running(self):
        while True:
            self.color = "Горит красный"
            print(f"{self.color}")
            sleep(7)
            self.color = "Горит жёлтый"
            print(f"{self.color}")
            sleep(2)
            self.color = "Горит зелёный"
            print(f"{self.color}")
            sleep(10)
            print("Горит жёлтый")
            sleep(2)


Traffic_Light = traffic_light()
Traffic_Light.running()
