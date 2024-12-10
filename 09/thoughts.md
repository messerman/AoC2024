# Part 1
* This seems pretty straightforward - but also its a really inefficient way of defragmenting the disk - since it splits up files. I have a feeling part 2 will ask us to do that aspect differently.
* They basically give you the algorithm in the question for this one, so I'm just going to straight-up implement it.
* For the first time this year, I submitted an answer that was wrong! Every other time, as long as it worked for sample.txt it has worked for index.txt, but not today
* if file_id > 9, my original code doesn't work, because I was storing it as ''.join(blocks)
* unfortuantely, the fix to that solution caused my algorithm to be significantly slower - I'm probably going to have to optimize to make part 2 work, whatever it ends up being....

# Part 2
* first thing's first - renaming `DiskMap.defrag()` to `DiskMap.reorder()`, and then making a NEW `defrag` method to do this part
* this was relatively straightforward to understand, but a pain to implement
* I ended up splitting `blocks` into `blanks` and `files`, and then zipping them back together to make it look like `blocks` from part 1
    * `zip`, in python, does not pad if the lists aren't as long as eachother, so had to use `itertools.zip_longest`
* basic algo was to start at the end of `files`, and then iterate through `blanks` until I found a blank size >= my file size
* had to change things at both ends of those lists to work
    * original blank section is replaced with `(0 blanks), (filesize file), (size_diff blanks)`
    * original file section is replaced with `(0 file), blank, (filesize blank)`
* got derailed for a while worrying about situations like `00...1..22..` (`231222`) which would turn into `00221.......`, which I thought should be represented as `2217`, but that didn't turn out to be a thing I had to worry about - possibly I would have needed to do so if I had actually bothered to clean up my class and make it "really" work, instead I just shoehorned in the checksum, and left the class in a messy state - should be easy enough to build some sort of function that could rebuild everything, but I'm tired of this problem