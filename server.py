#-*-coding:utf-8-*-
import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	'''  处理http request，send page.'''

	# 响应页面模版
	Page = '''\
	<html>
	<body>
	<table>
	<tr>  <td>Header</td>         <td>Value</td>          </tr>
	<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
	<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
	<tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
	<tr>  <td>Command</td>        <td>{command}</td>      </tr>
	<tr>  <td>Path</td>           <td>{path}</td>         </tr>
	</table>
	</body>
	</html>
	'''

	# 处理一个get请求
	def do_GET(self):
		page = self.create_page()
		self.send_page(page)

	# 渲染html
	def create_page(self):
		values = {
			'date_time'   : self.date_time_string(),
			'client_host' : self.client_address[0],
			'client_port' : self.client_address[1],
			'command'     : self.command,
			'path'        : self.path
		}
		page = self.Page.format(**values)
		return page

	# 发送页面
	def send_page(self, page):
		self.send_response(200)
		self.send_header('Content-Type','text.html')
		self.send_header("Content-Length", str(len(page)))
		self.end_headers()
		self.wfile.write(page)

if __name__ == '__main__':
	serverAddress = ('', 8080)
	server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
	server.serve_forever()


