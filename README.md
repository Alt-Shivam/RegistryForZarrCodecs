![image](https://user-images.githubusercontent.com/81817735/177476995-580fb2ed-0b4e-4bde-bfba-1fc70b044916.png)

# Registry (Zarr-Codecs)
## Created

2022-07-01
## Last Updated

2022-07-13
## Maintained By [Zarr-Developers](https://github.com/zarr-developers)

To know more about codecs, refer to this Research File

### [Link](https://alt-shivam.github.io/Codecs-Registry/Others/Research)
## Download this Registry
* [CSV](https://downgit.github.io/#/home?url=https://github.com/Alt-Shivam/Codecs-Registry/blob/main/Registry.csv)

## Registry

| **CodecID** | **CodecName** | **SourceCode** | **Type** | **Description** | **LastUpdate** |
|---|---|---|---|---|---|
| None | Checksum 32 | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/checksum32.py) | Numcodecs | Checksum Algorithm | 08/07/22 |
| None | Compat | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/compat.py) | Numcodecs |  | 08/07/22 |
| msgpack2 | MsgPack | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/msgpacks.py) | Numcodecs | Codec to encode data as msgpacked bytes. Useful for encoding an array of Python | 08/07/22 |
| base64 | Base64 | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/base64.py) | Numcodecs | Codec providing base64 compression via the Python standard library. | 08/07/22 |
| categorize | Categorize | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/categorize.py) | Numcodecs | Filter encoding categorical string data as integers. | 08/07/22 |
| delta | Delta | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/delta.py) | Numcodecs | Codec to encode data as the difference between adjacent values. | 08/07/22 |
| fixedscaleoffset | FixedScaleOffset | [Link]() | Numcodecs | Applies the transformation (x - offset) * scale to all chunks.  Results are rounded to the nearest integer | 08/07/22 |
| blosc | Blosc | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/blosc.pyx) | Numcodecs |  | 08/07/22 |
| gzip | GZIP | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/gzip.py) | Numcodecs | Codec providing gzip compression using zlib via the Python standard library. | 08/07/22 |
| bz2 | BZ2 | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/bz2.py) | Numcodecs | Codec providing compression using bzip2 via the Python standard library. | 08/07/22 |
| lzma | LZMA | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/lzma.py) | Numcodecs | Codec providing compression using lzma via the Python standard library. | 08/07/22 |
| lz4 | LZ4 | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/lz4.pyx) | Numcodecs |  | 08/07/22 |
| zlib | Zlib (DEFLATE) | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/zlib.py) | Numcodecs | Codec providing compression using zlib via the Python standard library. | 08/07/22 |
| zstd | ZStandard (ZSTD) | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/zstd.pyx) | Numcodecs |  | 08/07/22 |
| packbits | PackBits | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/packbits.py) | Numcodecs | Codec to pack elements of a boolean array into bits in a uint8 array. | 08/07/22 |
| pickle | Pickle | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/pickles.py) | Numcodecs | Codec to encode data as as pickled bytes. Useful for encoding an array of Python string objects. | 08/07/22 |
| quantize | Quantize | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/quantize.py) | Numcodecs | Lossy filter to reduce the precision of floating point data. | 08/07/22 |
| shuffle | Shuffle | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/_shuffle.pyx) | Numcodecs | Codec providing shuffle | 08/07/22 |
| zfpy | ZFPY | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/zfpy.py) | Numcodecs | Codec providing compression using zfpy via the Python standard library. | 08/07/22 |
| astype | Astype | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/astype.py) | Numcodecs | Filter to convert data between different types. | 08/07/22 |
| bitround | Bitround | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/bitround.py) | Numcodecs | Floating-point bit rounding codec | 08/07/22 |
| json2 | JSON | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/json.py) | Numcodecs | Codec to encode data as JSON. Useful for encoding an array of Python objects. | 08/07/22 |
| None | AEC | [Link]()* | ImageCodecs |  | 08/07/22 |
| None | APNG | [Link]()* | ImageCodecs |  | 08/07/22 |
| None | AVIF | [Link]()* | ImageCodecs |  | 08/07/22 |
| None | Brotli | [Link]()* | ImageCodecs |  | 08/07/22 |
| None | Brunsli | [Link]()* | ImageCodecs |  | 08/07/22 |
| None | LJpeg | [Link](https://github.com/libjpeg-turbo/libjpeg-turbo) | ImageCodecs |  | 04/08/22 |
| None | LZ4 | [Link](https://github.com/lz4/lz4) | ImageCodecs |  | 04/08/22 |
| None | MozJpeg | [Link](https://github.com/mozilla/mozjpeg) | ImageCodecs |  | 04/08/22 |
| None | Pglz | [Link]()* | ImageCodecs |  | 04/08/22 |
| None | Png | [Link](https://github.com/glennrp/libpng) | ImageCodecs |  | 04/08/22 |
| None | qoi | [Link](https://github.com/phoboslab/qoi) | ImageCodecs |  | 04/08/22 |
| None |  | [Link]()* | ImageCodecs |  | 04/08/22 |
| None | Deflate64 / Enhanced Deflate | [Link]()* | Others |  | 08/07/22 |
| None | Snappy | [Link]()* | Others |  | 08/07/22 |
| None | LZS | [Link]()* | Others |  | 08/07/22 |
| None | LZSS | [Link]()* | Others |  | 08/07/22 |
| None | LZO | [Link]()* | Others |  | 08/07/22 |
| None | LZFSE | [Link]()* | Others |  | 08/07/22 |
| None | ZFP | [Link]()* | Others |  | 08/07/22 |
| None | LZRW | [Link]()* | Others |  | 08/07/22 |
| None | LZX | [Link]()* | Others |  | 08/07/22 |
| None | LZWL | [Link]()* | Others |  | 08/07/22 |
| None | LZ4HC | [Link]()* | Others |  | 08/07/22 |
| None | LZW | [Link]()* | Others |  | 08/07/22 |
| None | LZF | [Link]()* | Others |  | 08/07/22 |
| None | GZIP | [Link]()* | Others |  | 08/07/22 |


## Haven't found your codec listed here?
You can easily add your codec by following these simple steps. :tada:
### Steps to follow.
**Step.1**- Make sure you have the Codec related information in the following manner.
```
* Blosc
- A brief about how the compression technique works(2-3 lines)
- Where the codec is primarily used(webpages, PNGs, JPEGs, OS etc.)
- Comparing compression and decompression benchmarks/speeds
- Any other info you think is useful
- Important links for the codec(GitHub, Blog post, Implementations etc.)

```

**Step.2**- Clone and make changes to these project files.

* clone the repo.
```bash
git clone https://github.com/Alt-Shivam/Codecs-Registry.git
```

* Add your codec information in Registry.csv file.

* Make changes to README.md file of branch gh-pages.

**Step.3**- Push your changes to your forked repo and Generate a Pull Request.

### Thanks for Visiting!!!
