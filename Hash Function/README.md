# Hash Function

## What is it?
A hash function is a mathematical algorithm that transforms any data into a byte-format array of fixed length. Each hash is unique, rendering them invaluable in information security, data storage, and machine learning. Currently, the SHA3-256 encoding is regarded as the standard, converting data into a 256-bit array.

I utilized the "hashlib" Python library to demonstrate the functionality of hash functions.

## Key characteristics
A hash function is deterministic; the same message will consistently yield the same hash.

####
```python
import hashlib

def becameHashSum(s):
    hash = hashlib.new('sha256')
    hash.update(s.encode())
    return  hash.hexdigest()

hash1 = becameHashSum('Lorem ipsum dolor sit amet, consectetur adipiscing elit')
hash2 = becameHashSum('Lorem ipsum dolor sit amet, consectetur adipiscing elit')

print(hash1) # output is 07fe4d4a25718241af145a93f890eb5469052e251d199d173bd3bd50c3bb4da2
print(hash2) # output is also 07fe4d4a25718241af145a93f890eb5469052e251d199d173bd3bd50c3bb4da2
```

It is exceedingly challenging, if not impossible, to find two distinct messages that produce the same hash value, given that there are 2 raised to the power of 256 possible variants for encoding data. This characteristic proves beneficial in identifying duplicates within datasets and crafting robust passwords.

Recovering data from a hash is infeasible, and even the slightest alteration in the input message results in a unrecognizable hash.

In the example below two strings are identical, but I added a period at the end of the second string, what has yielded an entirely distinct hash:
####
```python
hash1 = becameHashSum('Lorem ipsum dolor sit amet, consectetur adipiscing elit')
hash2 = becameHashSum('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(hash1) # output is 07fe4d4a25718241af145a93f890eb5469052e251d199d173bd3bd50c3bb4da2
print(hash2) # output is a58dd8680234c1f8cc2ef2b325a43733605a7f16f288e072de8eae81fd8d6433
```

## How it can be used in ML?
In machine learning, the application of hash functions enhances data processing speed and helps in identifying duplicate data. As array elements can be substantial, hash encoding significantly accelerates data handling.

For example::
####
```python
hash = becameHashSum("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nunc mi, finibus nec leo mattis, posuere bibendum lectus. Vestibulum tincidunt mauris quis orci ultricies, ac lobortis mauris rhoncus. Aliquam vulputate sollicitudin lacus, sed suscipit ex. Etiam facilisis interdum dictum. Fusce a dapibus erat, eu scelerisque velit. Etiam dolor diam, pretium nec ipsum sit amet, rutrum consequat dui. Mauris urna lorem, dictum sed convallis sed, tincidunt in orci. Proin interdum, felis in auctor suscipit, sapien nibh malesuada enim, nec viverra ex tellus eu leo. Nullam malesuada sit amet felis vitae tincidunt. Cras nec varius mauris. Sed egestas mauris vitae dolor vehicula maximus. Praesent in lacinia ante, sed pharetra quam. Sed dignissim lorem quis diam cursus vehicula. Mauris eu eros ullamcorper mi auctor convallis. Curabitur volutpat mollis dui sit amet commodo. Integer tincidunt scelerisque quam. Curabitur fermentum gravida blandit. Donec scelerisque et quam vel aliquet. In at elit tempus, porta quam eget, dictum dui. Etiam molestie facilisis sapien, in scelerisque turpis auctor sit amet. Praesent ultrices, quam id gravida laoreet, urna nunc condimentum tellus, eu tempus magna metus tincidunt nisl. Sed risus turpis, rutrum non sodales sit amet, consequat vel magna. Sed cursus purus et finibus scelerisque. Donec tristique diam imperdiet tortor blandit, vel convallis tellus tristique. Nullam eu sem sed arcu tempus egestas. Phasellus vehicula ex dolor, id euismod nisi rhoncus a. Curabitur dapibus ex non neque blandit, sed rhoncus leo egestas. Nam quis elit ultrices, euismod augue non, fringilla eros. Fusce fringilla dapibus elit sed ornare. Nulla vitae imperdiet quam, sit amet euismod libero. Nulla id sem ac lacus sagittis viverra. Mauris non ligula quis enim rhoncus pellentesque ut vel erat. Proin ut tincidunt mauris, eget placerat nunc. Proin imperdiet pretium ipsum quis viverra. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis sagittis ultrices. Sed luctus eros nisi, ut rutrum nisl iaculis a. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras condimentum imperdiet purus, id convallis magna euismod a. Vivamus ac pharetra sapien, eget ultricies orci. Donec ultricies quis lacus at efficitur. Nam eu sem quis orci laoreet fermentum. Quisque ut fermentum quam. Nullam aliquam blandit urna, non tempor leo egestas vitae. In tincidunt dictum erat, a euismod turpis dapibus a. Sed fermentum ac ligula sodales vehicula. Sed eget nisi non ex auctor efficitur sed vehicula turpis. Ut dapibus porttitor nisl, sed dictum lectus posuere sed. Vestibulum non tortor sodales, ultricies tortor eu, scelerisque eros. Curabitur id suscipit velit. Aliquam suscipit massa ac lacus viverra iaculis. Donec sed sollicitudin dolor, nec efficitur lectus. Nullam accumsan lacus in orci dignissim gravida eu et augue. Donec ut tristique felis. Morbi finibus feugiat vehicula. Fusce aliquet euismod lectus, quis mollis dolor volutpat et. Suspendisse tempus, elit ut luctus sagittis, tortor lectus commodo massa, quis consequat libero erat ac purus. In mollis a lacus vitae semper. Cras vestibulum, felis vel aliquet tincidunt, arcu purus gravida mi, sed condimentum elit neque vel odio. In hac habitasse platea dictumst. Nam eget rhoncus quam. Praesent mauris elit, pretium id justo at, condimentum malesuada enim. Nunc sollicitudin augue lacus, eget tempus diam aliquet in. Nullam tellus arcu, ultricies id diam ac, tempus egestas elit. Duis ultricies nec erat vitae luctus.")
print(hash) # output is 395109e4be3761ae2d610a634459c88324a4e9a0a1bbac286b087d95a89a15d5
```