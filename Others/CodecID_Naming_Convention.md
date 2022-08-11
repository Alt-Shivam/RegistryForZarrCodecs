# Naming Convention for Codec ID's. 

Currently, We have 2 different types of Codecs available in this **Codec Registry** i.e 
* NumCodecs
* ImageCodecs

The codecs from Numcodecs have already assigned with CodecID's, but Imagecodecs are not.  
So, For ImageCodecs without CodecID's, The naming convention is, as follows:

```
imagecodecs_{CodecName}
```

And For other codecs, the same will be:

```
organization_{CodecName}
```
**Or**
```
{CodecName}
```

### There is no need to assign a new codecID to those codecs which already have one.
