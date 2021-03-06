import ckan.lib.base as base
render = base.render

class AppsController(base.BaseController):

    def view(self):
        return render('offgridpages/apps.html')


class TermsController(base.BaseController):

    def view(self):
        return render('offgridpages/terms.html')

class PrivacyController(base.BaseController):

    def view(self):
        return render('offgridpages/privacy-policy.html')

# One controller per page.
# class AnotherController(base.BaseController):

#     def view(self):
#         return render('offgridpages/another.html')
