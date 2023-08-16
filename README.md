# pandoc_multi_docx_files

## 概要

マークアップ形式を変換するツール [Pandoc](https://github.com/jgm/pandoc/tree/main) を利用して，複数のWordファイル（.docx）をマークダウン形式に一括で変換するツールです．

## 使い方

1. 変換したいWordファイルを1つのディレクトリに格納し，make_md.pyも同じディレクトリに格納します．
2. make_md.pyを実行すると，mdfilesディレクトリが作成され，その中に変換したマークダウンファイルが格納されます．また，Wordファイル中の画像はmediaディレクトリ内のWordファイル名のディレクトリに格納されます．

## 注意点

- 画像ファイルの置かれる場所が生成されたmdファイル内の指定と異なるので，そのままでは画像が表示されません!!適宜修正してください．

## License

本プログラムで使用しているPandocのライセンスはGPL version 2であるため，本プログラムもGPL version 2となります．
