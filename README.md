![image](https://user-images.githubusercontent.com/81817735/177476995-580fb2ed-0b4e-4bde-bfba-1fc70b044916.png)

# Registry (Zarr-Codecs)  
Zarr is a chunked compressed format for the storage of N-dimensional arrays like those created by NumPy. Each compression algorithm used by Zarr is assigned an identifier by the numcodecs library. This registry makes these identifiers useful in other programming languages.  

## Download this Registry  
* [CSV](https://downgit.github.io/#/home?url=https://github.com/Alt-Shivam/Codecs-Registry/blob/main/Registry.csv)

## Registry

| **CodecID** | **CodecName** | **SourceCode** | **Type** | **Description** | **LastUpdate** |
|---|---|---|---|---|---|
| None | Checksum 32 | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/checksum32.py) | Numcodecs | Checksum Algorithm | 08/07/22 |
| msgpack2 | MsgPack | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/msgpacks.py) | Numcodecs | Codec to encode data as msgpacked bytes. Useful for encoding an array of Python | 08/07/22 |
| base64 | Base64 | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/base64.py) | Numcodecs | Codec providing base64 compression via the Python standard library. | 08/07/22 |
| categorize | Categorize | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/categorize.py) | Numcodecs | Filter encoding categorical string data as integers. | 08/07/22 |
| delta | Delta | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/delta.py) | Numcodecs | Codec to encode data as the difference between adjacent values. | 08/07/22 |
| fixedscaleoffset | FixedScaleOffset | [Link]() | Numcodecs | Applies the transformation (x - offset) * scale to all chunks.  Results are rounded to the nearest integer | 08/07/22 |
| blosc | Blosc | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/blosc.pyx) | Numcodecs | Codec providing compression using the Blosc meta-compressor. | 08/07/22 |
| gzip | GZIP | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/gzip.py) | Numcodecs | Codec providing gzip compression using zlib via the Python standard library. | 08/07/22 |
| bz2 | BZ2 | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/bz2.py) | Numcodecs | Codec providing compression using bzip2 via the Python standard library. | 08/07/22 |
| lzma | LZMA | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/lzma.py) | Numcodecs | Codec providing compression using lzma via the Python standard library. | 08/07/22 |
| lz4 | LZ4 | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/lz4.pyx) | Numcodecs | Codec providing compression using LZ4. | 08/07/22 |
| zlib | Zlib (DEFLATE) | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/zlib.py) | Numcodecs | Codec providing compression using zlib via the Python standard library. | 08/07/22 |
| zstd | ZStandard (ZSTD) | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/zstd.pyx) | Numcodecs | Codec providing compression using Zstandard. | 08/07/22 |
| packbits | PackBits | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/packbits.py) | Numcodecs | Codec to pack elements of a boolean array into bits in a uint8 array. | 08/07/22 |
| pickle | Pickle | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/pickles.py) | Numcodecs | Codec to encode data as as pickled bytes. Useful for encoding an array of Python string objects. | 08/07/22 |
| quantize | Quantize | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/quantize.py) | Numcodecs | Lossy filter to reduce the precision of floating point data. | 08/07/22 |
| shuffle | Shuffle | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/_shuffle.pyx) | Numcodecs | Codec providing shuffle | 08/07/22 |
| zfpy | ZFPY | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/zfpy.py) | Numcodecs | Codec providing compression using zfpy via the Python standard library. | 08/07/22 |
| astype | Astype | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/astype.py) | Numcodecs | Filter to convert data between different types. | 08/07/22 |
| bitround | Bitround | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/bitround.py) | Numcodecs | Floating-point bit rounding codec | 08/07/22 |
| json2 | JSON | [Link](https://github.com/zarr-developers/numcodecs/blob/main/numcodecs/json.py) | Numcodecs | Codec to encode data as JSON. Useful for encoding an array of Python objects. | 08/07/22 |
| None | AEC | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_aec.pyx) | ImageCodecs | Codec to implement the acoustic echo cancellation (AEC) and noise suppression (NS) algorithms. | 08/07/22 |
| None | APNG | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_apng.pyx) | ImageCodecs | APNG is a file format which extends the PNG specs to permit animated images that work similar to animated GIF files, while supporting 24-bit images and 8-bit transparency not available for GIFs.  | 08/07/22 |
| None | AVIF | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_avif.pyx) | ImageCodecs | AVIF is an image file format spec for storing images or image sequences compressed with AV1 in the HEIF container format. | 08/07/22 |
| None | Brotli | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_brotli.pyx) | ImageCodecs | lossless data compression algorithm which uses a combination of LZ77 lossless compression algorithm, Huffman coding and 2nd order context modelling. | 08/07/22 |
| None | Brunsli | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_brunsli.pyx) | ImageCodecs | Brunsli works as a transcoder converting between JPEG and JPEG XL. | 08/07/22 |
| None | LJpeg | [Link](https://github.com/libjpeg-turbo/libjpeg-turbo) | ImageCodecs | LJPEG is a mode of operation of JPEG. This mode exists because the discrete cosine transform (DCT) based form cannot guarantee that encoder input would exactly match decoder output. | 04/08/22 |
| None | MozJpeg | [Link](https://github.com/mozilla/mozjpeg) | ImageCodecs | MozJPEG improves JPEG compression efficiency achieving higher visual quality and smaller file sizes at the same time and compatible with the JPEG standard | 04/08/22 |
| None | Pglz | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_pglz.pyx) | ImageCodecs |  | 04/08/22 |
| None | Png | [Link](https://github.com/glennrp/libpng) | ImageCodecs | PNG is a raster-graphics file format that supports lossless data compression and supports palette-based images, grayscale images, and full-color non-palette-based RGB or RGBA images. | 04/08/22 |
| None | Qoi | [Link](https://github.com/phoboslab/qoi) | ImageCodecs | QOI is a specification for lossless image compression of 24-bit or 32-bit color raster (bitmapped) images. | 04/08/22 |
| None | Rcomp | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_rcomp.pyx) | ImageCodecs | Rcomp codec is an implementation of the Rice algorithm | 04/08/22 |
| None | SPng | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_spng.pyx) | ImageCodecs | Codec to convert numpy array to PNG image and vice versa. | 04/08/22 |
| None | Szip | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_szip.pyx) | ImageCodecs |  | 04/08/22 |
| None | Tiff | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_tiff.pyx) | ImageCodecs | Codec to convert numpy array to TIFF image and vice versa. | 04/08/22 |
| None | Webp | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_webp.pyx) | ImageCodecs | Codec to convert numpy array to WebP image. | 04/08/22 |
| None | ZLibng | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_zlibng.pyx) | ImageCodecs |  | 04/08/22 |
| None | Zopfli | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_zopfli.pyx) | ImageCodecs | Codec to Compress Zlib format using Zopfli. | 04/08/22 |
| None | Avif | [Link](https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_avif.pyx) | ImageCodecs | Codec to convert numpy array to  AVIF image. | 04/08/22 |
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

## To know more about codecs, refer to this Research File: [Link](https://alt-shivam.github.io/Codecs-Registry/Others/Research)

## CodecID Naming Convention: [Link](https://alt-shivam.github.io/Codecs-Registry/Others/CodecID_Naming_Convention.html)

## Created  
2022-07-01

## Last Updated  
2022-07-13

## Maintainer: [Zarr-Developers](https://github.com/zarr-developers)
### Author: [Shivank Chaudhary](https://github.com/Alt-Shivam)  

## To know more about codecs, refer to this Research File: [Link](https://alt-shivam.github.io/Codecs-Registry/Others/Research)

## Haven't found a codec listed here?
* [Add Now!](https://alt-shivam.github.io/Codecs-Registry/Others/AddNewCodec)

