
import os
import sys

def get_mdx_files(directory):
    """ディレクトリ以下の全ての.mdxファイルのパスを取得する"""
    mdx_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mdx') or file.endswith('.md'):
                mdx_files.append(os.path.join(root, file))
    return mdx_files

def make_separator(path, keyword):
    """特定のキーワード以降のパスを取得する"""
    try:
        # キーワードの位置を見つける
        index = path.index(keyword)
        # キーワード以降の部分文字列を抽出する
        return path[index:]
    except ValueError:
        # キーワードが見つからなかった場合は元のパスを返す
        return path

def concatenate_mdx_files(mdx_files, output_file, repo_name):
    """複数の.mdxファイルを結合して一つの大きな.mdxファイルを作成する"""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for mdx_file in mdx_files:
            separator = make_separator(os.path.relpath(mdx_file), repo_name)
            outfile.write(f"----------{separator}--------\n")
            with open(mdx_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")  # Ensure spacing between files

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <directory> <repository_name>\nexample: python main.py docs my-repo")
        sys.exit(1)

    docs_directory = sys.argv[1]
    if not os.path.isdir(docs_directory):
        print(f"The directory {docs_directory} does not exist or is not a directory.")
        sys.exit(1)
    repository_name = sys.argv[2]
    
    output_file = f'output/{repository_name}-combined.md'
    mdx_files = get_mdx_files(docs_directory)
    concatenate_mdx_files(mdx_files, output_file, repository_name)

if __name__ == '__main__':
    main()