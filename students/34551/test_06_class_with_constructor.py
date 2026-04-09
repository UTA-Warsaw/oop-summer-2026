class Lecture:
  def __init__(self, lecture, name, id, attendance):
    self.lecture = lecture
    self.name = name
    self.id = id
    self.attendance = attendance

p1 = Lecture("OOP", "Mustafa Selim Yildiz", "34551", True)

print((p1.lecture),(p1.name),(p1.id),(p1.attendance))
