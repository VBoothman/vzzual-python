import sys, os, re, time

# Checking dependencies
try:
    import pprint
    import json
    import vzzual
except ImportError, e:
    print "Unable to resolve dependency:\n %s" % e
    print '!pip install %s' % str(e).split()[-1]
    sys.exit(1)

# global variables
current_dir      = os.path.dirname(os.path.realpath(__file__))
API_KEY_FILENAME = os.path.join(current_dir, 'vzzual.conf')

# Exit if the api doesn't exit
if not os.path.exists(API_KEY_FILENAME):
    print "Please put your vzzual api key into a file called %s" % API_KEY_FILENAME
    sys.exit(1)

with open(API_KEY_FILENAME, 'r') as fp:
    token = fp.read().strip()

vzzual.init(token)
sample_image = os.path.join(current_dir, 'images/sample.jpg')

print "Creating Job .. "
req, results = vzzual.apply_image_filters(sample_image, ["facedetect", "exif", "thumbnail"])
state = req.state

if state == 'error':
    print "Got errors:"
    pprint.pprint(req.get_errors())

elif state == 'done':
    print "Got results:"
    pprint.pprint(results)

    ## Get filter result for thumbnail
    thumb = next(r for r in results if r['filter'] == 'thumbnail')['result']

    vfile = vzzual.File.find(thumb['thumbnail'])
    thumbnail_path = os.path.join(current_dir, 'images', 'thumbnail.jpg')

    print "Downloading thumbnail from %s .. " % vfile.file_url
    print "Saving thumbnail at %s ... " % thumbnail_path
    vfile.download(thumbnail_path)
