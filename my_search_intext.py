class My_Search_InText():
    def __init__(self, current_text = '', current_pos = 0, search_text = ''):
        self.textFind = current_text.lower()
        self.curr_pos = current_pos
        self.search_index = 0
        self.search_text = ''

    def searchIndex(self):
        return self.search_index

    def setSeacrhParams(self,current_text,current_pos):
        self.textFind = current_text.lower()
        self.curr_pos = current_pos

    def setSearchText(self,text):
        self.search_text = text.lower()

    def search(self):
        search_result = self.textFind.find(self.search_text,0)
        if search_result != -1:
            self.search_index = search_result

    def searchNext(self):
        startindex = self.curr_pos + len(self.search_text)
        search_result = self.textFind.find(self.search_text,startindex)
        if search_result != -1:
            self.search_index = search_result
        else:
            search_result = self.textFind.find(self.search_text,0)
            if search_result != -1:
                self.search_index = search_result
            else:
                self.search_index = 0

