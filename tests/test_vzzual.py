import json
import httpretty
from time import sleep
from nose2.compat import unittest
from nose.tools import assert_raises
from nose.plugins import attrib

import vzzual
content_type_json = 'application/json'
content_type_form = 'application/x-www-form-urlencoded'

def upload_file_callback(req, uri, headers):
    data = json.loads('{"tags": [], "filesize": 357287, "created": "2013-10-17T17:39:01.471Z", "url": "https://api.vzzual.com/files/2PRcFB54AcB", "original_name": "sample3.jpg", "original_url": "<url>", "file_url": "<removed>", "id": "2PRcFB54AcB", "visibility": "private", "modified": "2013-10-17T17:39:01.471Z"}')

    if isinstance(req.parsed_body, dict):
        data['visibility'] = req.parsed_body.get('visibility', 'private')
        if 'url' in req.parsed_body:
            data['original_url'] = req.parsed_body['url']

    return [200, headers, json.dumps(data)]


def mock_new_request():
    httpretty.enable()

    body = '{"tags": ["test_tag", "second_tag"], "logs_url": "https://api.vzzual.com/requests/2PRcFApXydQ/logs/", "files_url": "https://api.vzzual.com/requests/2PRcFApXydQ/files/", "cost": 0.01, "filters": [{"filter": "facedetect", "config": ""}, {"filter": "image_info", "config": ""}], "results_url": "https://api.vzzual.com/requests/2PRcFApXydQ/results/", "callback": "", "priority": "normal", "created": "2013-10-17T17:25:37.801Z", "url": "https://api.vzzual.com/requests/2PRcFApXydQ", "modified": "2013-10-17T17:25:38.294Z", "submit_url": "https://api.vzzual.com/requests/2PRcFApXydQ/submit", "errors_url": "https://api.vzzual.com/requests/2PRcFApXydQ/errors/", "state": "new", "time": 1.0}'
    httpretty.register_uri(httpretty.POST, vzzual.base_url + "requests/", body,
                  content_type=content_type_json)

    mock_request_result()

    httpretty.register_uri(httpretty.DELETE,
                          'https://api.vzzual.com/requests/2PRcFApXydQ',
                          '{"success" : "true" }')

    files = '{"count": 6, "previous": "null", "results": [{"tags": [], "filesize": 387280, "created": "2013-09-17T05:18:54.377Z", "url": "https://api.vzzual.com/files/2PRcFAoEZQu", "original_name": "sample.jpg", "original_url": "", "file_url": "<removed>", "id": "2PRcFAoEZQu", "visiblity": "private", "modified": "2013-09-17T05:18:54.377Z"}, {"tags": [], "filesize": 489, "created": "2013-10-17T17:34:36.702Z", "url": "https://api.vzzual.com/files/2PRcFAotjoJ", "original_name": "sample2.jpg", "original_url": "", "file_url": "<removed>", "id": "2PRcFAotjoJ", "visibility": "private", "modified": "2013-10-17T17:34:36.702Z"}], "next": "https://api.vzzual.com/files/?page=2"}'
    file_data = '{"tags": [], "filesize": 357287, "created": "2013-10-17T17:39:01.471Z", "url": "https://api.vzzual.com/files/2PRcFB54AcB", "original_name": "sample3.jpg", "original_url": "<url>", "file_url": "<removed>", "id": "2PRcFB54AcB", "visibility": "private", "modified": "2013-10-17T17:39:01.471Z"}'

    httpretty.register_uri(httpretty.POST,
                  'https://api.vzzual.com/requests/2PRcFApXydQ/files/',
                  body=upload_file_callback,
                  content_type=content_type_json)

    httpretty.register_uri(httpretty.GET,
                  'https://api.vzzual.com/requests/2PRcFApXydQ/files/', files,
                  content_type=content_type_json)

    httpretty.register_uri(httpretty.PUT,
                  'https://api.vzzual.com/requests/2PRcFApXydQ/submit',
                  file_data,
                  content_type=content_type_json)

    httpretty.register_uri(httpretty.GET,
                            "https://api.vzzual.com/files/2PRcFB54AcB",
                            files,
                            content_type=content_type_json)

    mock_files()

def mock_files():
    httpretty.enable()
    httpretty.register_uri(httpretty.POST, vzzual.base_url + "files/",
                            body=upload_file_callback,
                            content_type='application/octec-stream')

    httpretty.register_uri(httpretty.DELETE,
                            "https://api.vzzual.com/files/2PRcFB54AcB",
                            '{"success" : "true" }')


def mock_request_result():
    httpretty.enable()
    _first_req = True
    body1 = '{"tags": ["test_tag", "second_tag"], "logs_url": "https://api.vzzual.com/requests/2PRcFApXydQ/logs/", "files_url": "https://api.vzzual.com/requests/2PRcFApXydQ/files/", "cost": 0.01, "filters": [{"filter": "facedetect", "config": ""}, {"filter": "image_info", "config": ""}], "results_url": "https://api.vzzual.com/requests/2PRcFApXydQ/results/", "callback": "", "priority": "normal", "created": "2013-10-17T17:25:37.801Z", "url": "https://api.vzzual.com/requests/2PRcFApXydQ", "modified": "2013-10-17T17:25:38.294Z", "submit_url": "https://api.vzzual.com/requests/2PRcFApXydQ/submit", "errors_url": "https://api.vzzual.com/requests/2PRcFApXydQ/errors/", "state": "created", "time": 1.0}'
    body2 = '{"tags": ["test_tag", "second_tag"], "logs_url": "https://api.vzzual.com/requests/2PRcFApXydQ/logs/", "files_url": "https://api.vzzual.com/requests/2PRcFApXydQ/files/", "cost": 0.01, "filters": [{"filter": "facedetect", "config": ""}, {"filter": "image_info", "config": ""}], "results_url": "https://api.vzzual.com/requests/2PRcFApXydQ/results/", "callback": "", "priority": "normal", "created": "2013-10-17T17:25:37.801Z", "url": "https://api.vzzual.com/requests/2PRcFApXydQ", "modified": "2013-10-17T17:25:38.294Z", "submit_url": "https://api.vzzual.com/requests/2PRcFApXydQ/submit", "errors_url": "https://api.vzzual.com/requests/2PRcFApXydQ/errors/", "state": "done", "time": 1.0}'

    def is_first_request():
        return _first_req

    def first_request_done():
        _first_req = False

    def on_request_url(req, uri, headers):
        print "\n{}: {}\n".format(uri, is_first_request())
        if is_first_request():
            first_request_done()
            return [200, headers, body2]
        else:
            sleep(2)
            return [200, headers, body2]

    httpretty.register_uri(httpretty.GET, 'https://api.vzzual.com/requests/2PRcFApXydQ',
                            body=on_request_url,
                            content_type=content_type_json)

    result = '{"count": 1, "previous": "null", "results": [{"filter": "facedetect", "result": "[[686,241,38,38],[217,145,39,39],[330,183,39,39],[532,188,36,36],[106,161,43,43],[588,240,41,41],[492,231,44,44]]", "file": "2PRcFB5frdf"}, {"filter": "image_info", "result": "{\\"width\\":1024,\\"format\\": \\"JPEGn\\",\\"height\\":678,\\"moden\\":\\"RGBn\\"}", "file": "24pwm6t8havzf"}], "next": "null"}'

    httpretty.register_uri(httpretty.GET,
                            'https://api.vzzual.com/requests/2PRcFApXydQ/results/',
                            result,
                            content_type=content_type_json)


def mock_filters():
    httpretty.enable()
    body = '{"count": 2, "previous": "null", "results": [{"time": 1.0, "cost": 0.01, "name": "facedetect", "description": "Detect faces in images, returning the detected x/y position and width/height of each face."}, {"time": 0.1, "cost": 0.01, "name": "image_info", "description": "Extract basic image information (width, height, format, mode)."}], "next": "null"}'
    httpretty.register_uri(httpretty.GET, vzzual.base_url + "filters/", body,
                           content_type=content_type_json)

class TestBase(unittest.TestCase):
    def setUp(self):
        vzzual.init('abc')

    def test_get_filters(self):
        mock_filters()
        filters = [fobject['name'] for fobject in vzzual.get_filters()]
        self.assertEqual(filters[0], 'facedetect')
        self.assertEqual(filters[1], 'image_info')


    def test_set_api_key(self):
        vzzual.init(None)
        assert_raises(RuntimeError, vzzual.get_filters)

    def test_requests(self):
        mock_new_request()
        req = vzzual.Request.create(filters=[{'filter' : 'facedetect'}])
        self.assertEqual(req.state, 'new')
        req2 = vzzual.Request.find(req.url)
        self.assertEqual(req.url, req2.url)
        req.delete()


    def test_request_submit(self):
        mock_new_request()
        req =  vzzual.Request.create(filters=[{'filter' : 'facedetect'}])
        req.add_files(['tests/test.jpg'], 'private')
        req.submit()
        res = req.get_results(wait=True)[0]
        self.assertEqual(res['filter'], 'facedetect')
        self.assertIsNotNone(res['result'])
        req.delete()


    def test_add_files(self):
        mock_new_request()
        req = vzzual.Request.create(filters=[{'filter' : 'facedetect'}])
        req.add_files('tests/test.jpg')
        req_file = req.get_files()[0]
        self.assertIsNotNone(req_file.id)
        self.assertIsNotNone(req_file.url)
        self.assertIsNotNone(req_file.file_url)
        req.delete()


    def test_add_files_with_urls(self):
        mock_new_request()
        req = vzzual.Request.create(filters=[{'filter' : 'facedetect'}])
        urls = [
            'http://upload.wikimedia.org/wikipedia/commons/b/b9/Steve_Jobs_Headshot_2010-CROP.jpg',
            'http://upload.wikimedia.org/wikipedia/commons/5/58/Stevejobs_Macworld2005.jpg'
        ]
        req_files = req.add_files(urls)
        self.assertEqual(len(req_files), 2)
        f1, f2 = req_files
        self.assertIsNotNone(f1.id)
        self.assertEqual(f1.original_url, urls[0])
        self.assertIsNotNone(f2.id)
        self.assertEqual(f2.original_url, urls[1])
        req.delete()


    def test_create_files(self):
        mock_files()
        ffile = vzzual.File.create(image='tests/test.jpg', visibility='public')
        self.assertIsNotNone(ffile.id)
        self.assertIsNotNone(ffile.url)
        ffile.delete()

    def test_create_file_with_url(self):
        mock_files()
        url = 'http://upload.wikimedia.org/wikipedia/commons/b/b9/Steve_Jobs_Headshot_2010-CROP.jpg'
        ffile = vzzual.File.create(url=url)
        self.assertIsNotNone(ffile.id)
        self.assertIsNotNone(ffile.original_url, url)
        ffile.delete()

    def test_apply_image_filters(self):
        mock_filters()
        mock_new_request()
        req, res = vzzual.apply_image_filters('tests/test.jpg',
                                             ['facedetect','image_info'] )
        req.delete()
        self.assertEqual(req.state, 'done')
        self.assertIsNotNone(res)


