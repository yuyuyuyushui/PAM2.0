from core.rest_client import *

class PersonalCenter(RestClient):

    def Get_basic_information(self,tenantId,**kwargs):
        return self.get("/v2/tenement/tenant/{}/info/base".format(tenantId), **kwargs)

    def List_of_tenants_owned(self,tenantId,**kwargs):
        return self.get("/v2/tenement/tenant/{}/info/tenement".format(tenantId),**kwargs)

    def Current_session_track(self,tenantId,**kwargs):
        return self.get("/v2/tenement/tenant/{}/info/trace".format(tenantId),**kwargs)

    def Modify_personal_information(self,tenantId,**kwargs):
        return self.patch("/v2/tenement/tenant/{}/info/base".format(tenantId),**kwargs)