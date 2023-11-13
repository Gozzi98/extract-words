import argparse
import random
import json

"""Write a script extract_to_tsv.py that accepts one of the files you collected from Reddit and outputs 
a random selection of posts from that file to a tsv (tab separated value) file.  
It should function like this:

	python3 extract_to_tsv.py -o <out_file> <json_file> <num_posts_to_output>

If <num_posts_to_output> is greater than the file length, then the script should just output all lines. 
 If there are more than <num_posts_to_output> (which is likely the case), then it should randomly 
 select num_posts_to_output (the parameter you passed to the script) of them and just output those.


"""
#seems like post are not unique , question to ask ta or prof
def extract_to_tsv(json_file, num_posts_to_output, out_file):
    """Extracts a random selection of posts from a json file and outputs them to a tsv file

    Args:
        json_file (str): The json file to extract posts from
        num_posts_to_output (int): The number of posts to output
        out_file (str): The name of the tsv file to output to
    """
    #select random posts    
    with open(json_file, 'r') as f:
        posts = json.load(f)
    #get a list of posts
    posts_list = posts["data"]["children"]
    #select random posts
    random_posts = []
    while len(random_posts) < num_posts_to_output:
        post = random.choice(posts_list)
        if post not in random_posts:
            random_posts.append(post)
    #random_posts = [random.choice(posts_list) for _ in range(min(num_posts_to_output, len(posts_list)))]
    #write to tsv file
    with open(out_file, 'w') as tsv:
        tsv.write('Name\ttitle\tcoding\n')
        list_names = []
        for post in random_posts:
            try:
                post_name = post['data']['name']
                post_title = post['data']['title']
                
                tsv.write(f"{post_name}\t{post_title}\n")
            except KeyError as e:
                print(f"Skipping post due to missing key: {e}")
def main():
    argparser = argparse.ArgumentParser(description='Extracts a random selection of posts from a json file and outputs them to a tsv file')
    argparser.add_argument('-o', '--out_file', help='The name of the tsv file to output to')
    argparser.add_argument('json_file', help='The json file to extract posts from')
    argparser.add_argument('num_posts_to_output',type=int, help='The number of posts to output')
    args = argparser.parse_args()
    extract_to_tsv(args.json_file, args.num_posts_to_output, args.out_file)


if __name__ == '__main__':
    main()

