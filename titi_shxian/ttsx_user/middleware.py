class UrlMiddleware:
    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.path not in['/user/register/',
                               '/user/register_handle/',
                               '/user/register_valid/',
                               '/user/login/',
                               '/user/login_handle/',
                               '/user/logout/',
                               '/user/islogin/',]:
            request.session['url_path']=request.get_full_path()
                               

        
        
                                          
                              
