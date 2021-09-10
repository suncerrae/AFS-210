class Node:
    def __init__(self, data):
        self.data = data
        self.nextdata = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def AddItem(self, addData):
        New = Node(addData)
        New.nextdata = self.head
        self.head = New
		

    def RemoveItem(self, removeData):

        headData = self.head

        if (headData is not None):
            if (headData.data == removeData):
                self.head = headData.nextdata
                headData = None
                return

        while (headData is not None):
            if headData.data == removeData:
                break
            prev = headData
            headData = headData.nextdata

        if (headData == None):
            return

        prev.nextdata = headData.nextdata

        headData = None

    def PrintList(self):
        printdata = self.head
        while (printdata):
            print(printdata.data),
            printdata = printdata.nextdata


link = MyLinkedList()
link.AddItem("Java")
link.AddItem("C++")
link.AddItem("C#")
link.AddItem("Python")
link.AddItem("PHP")

link.PrintList()
link.RemoveItem("C#")
link.PrintList()