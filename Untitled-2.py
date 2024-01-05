class BoardingPass:
    def __init__(self, passenger_name, boarding_code, boarding_time, gate_number, seat_location, luggage_count, luggage_ids):
        self.passenger_name = passenger_name
        self.boarding_code = boarding_code
        self.boarding_time = boarding_time
        self.gate_number = gate_number
        self.seat_location = seat_location
        self.luggage_count = luggage_count
        self.luggage_ids = luggage_ids

    def describe(self):
        print("登機證資訊：")
        print(f"旅客姓名：{self.passenger_name}")
        print(f"登機護編號：{self.boarding_code}")
        print(f"登機時間：{self.boarding_time}")
        print(f"登記門編號：{self.gate_number}")
        print(f"座位位置：{self.seat_location}")
        print(f"行李數量：{self.luggage_count}")
        print(f"行李ID：{', '.join(self.luggage_ids)}")

    def update_passenger_name(self, new_name):
        self.passenger_name = new_name

    def update_boarding_code(self, new_code):
        self.boarding_code = new_code

    def update_boarding_time(self, new_time):
        self.boarding_time = new_time

    def update_gate_number(self, new_gate):
        self.gate_number = new_gate

    def update_seat_location(self, new_seat):
        self.seat_location = new_seat


class Luggage:
    def __init__(self, luggage_id, weight, departure_airport, destination_airport):
        self.luggage_id = luggage_id
        self.weight = weight
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport

    def describe(self):
        print("行李資訊：")
        print(f"行李ID：{self.luggage_id}")
        print(f"行李重量：{self.weight} 公斤")
        print(f"行李出發機場：{self.departure_airport}")
        print(f"行李目的地機場：{self.destination_airport}")

    def update_luggage_id(self, new_id):
        self.luggage_id = new_id

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_departure_airport(self, new_departure):
        self.departure_airport = new_departure

    def update_destination_airport(self, new_destination):
        self.destination_airport = new_destination


def query_luggage_information(luggage_list, luggage_id):
    for luggage in luggage_list:
        if luggage.luggage_id == luggage_id:
            luggage.describe()
            return
    print(f"行李ID {luggage_id} 的行李未找到。")

# 創建登機證和行李的實例
boarding_passenger1 = BoardingPass("Alice", "ABC123", "12:00 PM", "Gate A1", "23B", 2, ["L001", "L002"])
boarding_passenger2 = BoardingPass("Bob", "XYZ789", "1:30 PM", "Gate B3", "15C", 1, ["L003"])

luggage1 = Luggage("L001", 18, "機場 X", "機場 Y")
luggage2 = Luggage("L002", 22, "機場 X", "機場 Y")
luggage3 = Luggage("L003", 15, "機場 Z", "機場 X")

# 使用 describe 方法顯示登機證和行李資訊
boarding_passenger1.describe()
luggage1.describe()

# 修改登機證和行李的資訊
boarding_passenger1.update_passenger_name("小黃")
boarding_passenger1.update_boarding_code("XYZ987")
luggage1.update_weight(20)

# 重新顯示修改後的登機證和行李資訊
boarding_passenger1.describe()
luggage1.describe()

# 查詢行李資訊
query_luggage_information([luggage1, luggage2, luggage3], "L002")