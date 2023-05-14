import subprocess
import pathlib

def main():
    # このファイルのディレクトリを取得する
    current_dir = pathlib.Path(__file__).resolve().parent
    
    # .docx形式のファイル名を取得する
    docx_files = list(current_dir.glob('*.docx'))
    
    # markdownはサブディレクトリmdfilesに保存する
    # mdfilesが存在するか確認し，なければ作成する
    md_save_dir = current_dir.joinpath('mdfiles')
    if not md_save_dir.exists():
        md_save_dir.mkdir()
    fig_save_dir = current_dir.joinpath('media')
    if not fig_save_dir.exists():
        fig_save_dir.mkdir()
    
    # pandocを実行する
    for docx_file in docx_files:
        md_file = md_save_dir.joinpath(docx_file.stem + '.md')
        fig_dir = fig_save_dir.joinpath(docx_file.stem)
        extract_media_command = '--extract-media=' + str(fig_dir)
        subprocess.run(['pandoc', str(docx_file), '--wrap=none', extract_media_command, '-o', str(md_file)])
        
        # 画像ファイルがあるか判別する
        if fig_dir.exists():
            # 画像ファイルを1つ上のディレクトリに移動する
            for fig_file in fig_dir.glob('media/*'):
                if not fig_dir.joinpath(fig_file.name).exists():
                    fig_file.rename(fig_dir.joinpath(fig_file.name))
                else:
                    fig_file.unlink()
            fig_dir.joinpath('media').rmdir()

if __name__ == '__main__':
    main()