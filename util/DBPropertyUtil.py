class PropertyUtil:
    connection_properties= None

    @staticmethod
    def getConnectionString():
        if PropertyUtil.connection_properties is None:
            host='localhost'
            database='cars'
            user='root'
            password='Muskan20'
            PropertyUtil.connection_properties={'host':host,'database':database,'user':user,'password':password}
        return  PropertyUtil.connection_properties