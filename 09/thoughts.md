# Part 1
* This seems pretty straightforward - but also its a really inefficient way of defragmenting the disk - since it splits up files. I have a feeling part 2 will ask us to do that aspect differently.
* They basically give you the algorithm in the question for this one, so I'm just going to straight-up implement it.
* For the first time this year, I submitted an answer that was wrong! Every other time, as long as it worked for sample.txt it has worked for index.txt, but not today
* if file_id > 9, my original code doesn't work, because I was storing it as ''.join(blocks)
* unfortuantely, the fix to that solution caused my algorithm to be significantly slower - I'm probably going to have to optimize to make part 2 work, whatever it ends up being....

# Part 2
* 