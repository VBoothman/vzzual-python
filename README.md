python-vzzual
=============

python-vzzual is a python client for [Vzzual](http://vzzual.com)

## Documentation

Documentation is available at [http://www.vzzual.com/page_API.html](http://www.vzzual.com/page_API.html)

## How to use

```sh
    import vzzual
    vzzual.init('<api_key>', log_level=logging.DEBUG)
    req = vzzual.Request.create(
                    filters=[{ 'filter': 'facedetect' }, { 'filter': 'exif' }])
    req.add_files('image.jpg')
    req.submit()
    results = req.get_results(wait=True)
```

## How to test

1. Dump your vzzual api key into vzzual.conf

2. Install the dependencies
  ```sh
    $] cd SDK/Python
    $] pip install -r requirements.txt
  ```

3. Run the tests
  ```sh
    $] nose2
  ```
