class ReportError:
    def __init__(self, list_errors):
        self.list_errors = list_errors
    
    def get_report(self):
        file_content = ""
        file_content += self.header()
        file_content += '<title>Errors</title>'
        file_content += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n\t'
        file_content += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n\t'
        file_content += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n\t'
        file_content += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n\t'
        file_content += '</head>'
        file_content += '<body style="background-color: green;">'
        file_content += '<div class=\"container\"><br>'
        file_content += '<h1 style="text-align: center; color: aqua; background-color: blue;">List of Errors</h1><hr>'
        file_content += '<table id=\"example\"  class="table" style="background-color: cadetblue;">'
        file_content += '<thead  class="thead-dark" ><tr><th>#</th><th>Type</th><th>Description</th><th>Row</th><th>Column</th></tr></thead>'
        file_content += '<tbody>'
        file_content += self.get_content_report()
        file_content += '</tbody>'
        file_content += '</table>'
        file_content += '</div>'
        file_content += self.footer()
        return file_content
        
    def header(self):
        file_content = ''
        file_content += '<!doctype html>'
        file_content += '<html lang=\"es\">'
        file_content += '<head>'
        file_content += '<meta charset=\"utf - 8\">'
        file_content += '<meta name=\"viewport\" content=\"width = device - width, initial - scale = 1, shrink - to - fit = no\">'
        file_content += '<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.css\">'
        file_content += '<link rel=\"stylesheet\" href=\"https://cdn.datatables.net/1.10.20/css/dataTables.bootstrap4.min.css\">'
        return file_content
    
    def footer(self):
        file_content = ''
        file_content += '<script src=\"https://code.jquery.com/jquery-3.3.1.js\"></script>'
        file_content += '<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js\"></script>'
        file_content += '<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js\"></script>'
        file_content += '<script src=\"https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js\"></script>'
        file_content += '<script src=\"https://cdn.datatables.net/1.10.20/js/dataTables.bootstrap4.min.js\"></script>'
        file_content += '''<script> $(document).ready(function () {$(\'#example\').DataTable();});</script>'''
        file_content += '</body>'
        file_content += '</html>'
        return file_content

    def get_content_report(self):
        file_content = ""
        values = self.list_errors.head_value
        while values is not None:
            file_content += "<TR>"
            file_content += "<TH>" + str(values.data.get_id()) + "</TH>"
            file_content += "<TH>" + values.data.get_type() + "</TH>"
            file_content += "<TH>" + values.data.get_description() + "</TH>"
            file_content += "<TH>" + str(values.data.get_row()) + "</TH>"
            file_content += "<TH>" + str(values.data.get_column()) + "</TH>"
            file_content += "</TR>"
            values = values.next
        return file_content

