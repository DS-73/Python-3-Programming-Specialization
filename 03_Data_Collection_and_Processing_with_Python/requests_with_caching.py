import requests
import json

PERMANENT_CACHE_FNAME = "./assets/permanent_cache.txt"
TEMP_CACHE_FNAME = "this_page_cache.txt"

def _write_to_file(cache, fname):
    with open(fname, 'w') as outfile:
        outfile.write(json.dumps(cache, indent=2))

def _read_from_file(fname):
    try:
        with open(fname, 'r') as infile:
            res = infile.read()
            return json.loads(res)
    except:
        return {}

def add_to_cache(cache_file, cache_key, cache_value):
    temp_cache = _read_from_file(cache_file)
    temp_cache[cache_key] = cache_value
    _write_to_file(temp_cache, cache_file)

def clear_cache(cache_file=TEMP_CACHE_FNAME):
    _write_to_file({}, cache_file)

def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url    
    
def make_cache_key(baseurl, params_d, private_keys=["api_key", "apikey"]):
    """Makes a long string representing the query.
    Alphabetize the keys from the params dictionary so we get the same order each time.
    Omit keys with private info."""
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            val = params_d[k]
            if type(val) == list:
                val = ','.join([str(item) for item in val])
                print(val)
            res.append("{}-{}".format(k, val))
    return baseurl + "_".join(res)

def perm_cache():
    return _read_from_file(PERMANENT_CACHE_FNAME)

def get(baseurl, params={}, private_keys_to_ignore=["api_key", "apikey"], permanent_cache_file=PERMANENT_CACHE_FNAME, temp_cache_file=TEMP_CACHE_FNAME, headers=None):
    full_url = requestURL(baseurl, params)
    cache_key = make_cache_key(baseurl, params, private_keys_to_ignore)
    # Load the permanent and page-specific caches from files
    permanent_cache = _read_from_file(permanent_cache_file)
    temp_cache = _read_from_file(temp_cache_file)
    if cache_key in temp_cache:
        print("found in page-specific cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        resp = requests.Response()
        resp._content = bytes(temp_cache[cache_key], 'utf-8')
        resp.url = full_url
        return resp
    elif cache_key in permanent_cache:
        print("found in permanent_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        resp = requests.Response()
        resp._content = bytes(permanent_cache[cache_key], 'utf-8')
        resp.url = full_url
        return resp
    else:
        print("new; adding to cache")
        # actually request it
        resp = requests.get(baseurl, params, headers=headers)
        # save it
        add_to_cache(temp_cache_file, cache_key, resp.text)
        return resp