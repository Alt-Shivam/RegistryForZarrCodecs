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
| None | AEC | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_aec.pyx) | ImageCodecs |  | 08/07/22 |
| None | APNG | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_apng.pyx) | ImageCodecs | APNG is a file format which extends the PNG specs to permit animated images that work similar to animated GIF files, while supporting 24-bit images and 8-bit transparency not available for GIFs.  | 08/07/22 |
| None | AVIF | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_avif.pyx) | ImageCodecs | AVIF is an image file format spec for storing images or image sequences compressed with AV1 in the HEIF container format. | 08/07/22 |
| None | Brotli | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_brotli.pyx) | ImageCodecs | lossless data compression algorithm which uses a combination of LZ77 lossless compression algorithm, Huffman coding and 2nd order context modelling. | 08/07/22 |
| None | Brunsli | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_brunsli.pyx) | ImageCodecs |  | 08/07/22 |
| None | LJpeg | [Link](https://github.com/libjpeg-turbo/libjpeg-turbo) | ImageCodecs |  | 04/08/22 |
| None | MozJpeg | [Link](https://github.com/mozilla/mozjpeg) | ImageCodecs |  | 04/08/22 |
| None | Pglz | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_pglz.pyx) | ImageCodecs |  | 04/08/22 |
| None | Png | [Link](https://github.com/glennrp/libpng) | ImageCodecs |  | 04/08/22 |
| None | Qoi | [Link](https://github.com/phoboslab/qoi) | ImageCodecs |  | 04/08/22 |
| None | Rcomp | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_rcomp.pyx) | ImageCodecs |  | 04/08/22 |
| None | Shared | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_shared.pyx) | ImageCodecs |  | 04/08/22 |
| None | SPng | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_spng.pyx) | ImageCodecs |  | 04/08/22 |
| None | Szip | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_szip.pyx) | ImageCodecs |  | 04/08/22 |
| None | Tiff | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_tiff.pyx) | ImageCodecs |  | 04/08/22 |
| None | Webp | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_webp.pyx) | ImageCodecs |  | 04/08/22 |
| None | ZLibng | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_zlibng.pyx) | ImageCodecs |  | 04/08/22 |
| None | Zopfli | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_zopfli.pyx) | ImageCodecs |  | 04/08/22 |
| None | Avif | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_avif.pyx) | ImageCodecs |  | 04/08/22 |
| None | Cms | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_cms.pyx) | ImageCodecs |  | 04/08/22 |
| None | Deflate | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_deflate.pyx) | ImageCodecs |  | 04/08/22 |
| None | Gif | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_gif.pyx) | ImageCodecs |  | 04/08/22 |
| None | Heif | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_heif.pyx) | ImageCodecs |  | 04/08/22 |
| None | Jetraw | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_jetraw.pyx) | ImageCodecs |  | 04/08/22 |
| None | Jpeg12 | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_jpeg12.pyx) | ImageCodecs |  | 04/08/22 |
| None | Jpeg2k | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_jpeg2k.pyx) | ImageCodecs |  | 04/08/22 |
| None | Jpeg8 | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_jpeg8.pyx) | ImageCodecs |  | 04/08/22 |
| None | Jpegls | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_jpegls.pyx) | ImageCodecs |  | 04/08/22 |
| None | Jpegsof3 | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_jpegsof3.pyx) | ImageCodecs |  | 04/08/22 |
| None | Jpegxl | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_jpegxl.pyx) | ImageCodecs |  | 04/08/22 |
| None | Jpegxr | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_jpegxr.pyx) | ImageCodecs |  | 04/08/22 |
| None | Lerc | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_lerc.pyx) | ImageCodecs |  | 04/08/22 |
| None | Deflate64 / Enhanced Deflate | [Link](https://github.com/brianhelba/zipfile-deflate64) | Others |  | 08/07/22 |
| None | Snappy | [Link](https://github.com/google/snappy) | Others |  | 08/07/22 |
| None | LZS | [Link](https://github.com/m-boutaleb/LZS) | Others |  | 08/07/22 |
| None | LZSS | [Link](https://github.com/MichaelDipperstein/lzss) | Others |  | 08/07/22 |
| None | LZO | [Link](https://github.com/nemequ/lzo) | Others |  | 08/07/22 |
| None | LZFSE | [Link](https://github.com/lzfse/lzfse) | Others |  | 08/07/22 |
| None | ZFP | [Link](https://github.com/LLNL/zfp) | Others |  | 08/07/22 |
| None | LZRW | [Link]()* | Others |  | 08/07/22 |
| None | LZX | [Link]()* | Others |  | 08/07/22 |
| None | LZWL | [Link]()* | Others |  | 08/07/22 |
| None | LZ4HC | [Link](https://github.com/bwlewis/lz4) | Others |  | 08/07/22 |
| None | LZW | [Link]()* | Others |  | 08/07/22 |
| None | LZF | [Link](https://github.com/nemequ/liblzf) | Others |  | 08/07/22 |
| None | GZIP | [Link](https://github.com/kunpengcompute/gzip) | Others |  | 08/07/22 |


## Haven't found a codec listed here?
* [Add Now!](https://alt-shivam.github.io/Codecs-Registry/Others/AddNewCodec)

