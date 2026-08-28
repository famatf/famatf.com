# famatf.com

这是 `famatf.com` 的 Jekyll 源码，使用
[`no-style-please`](https://github.com/riggraz/no-style-please) 主题与 KaTeX。
为保证构建稳定和离线预览，主题文件固定于上游提交
`2f8dba2c23633b21e45dce0fe2e34ec2d79bb1ca` 并随仓库保存。

## 内容目录

- `_posts/notes/`：有发布日期的学习笔记与计算文章。
- `_posts/writing/`：以后新增的随笔、评论及其他写作。
- `assets/images/gallery/`：Gallery 使用的图片。
- `about.md`、`gallery.md`：独立页面。

Jekyll 文章文件名使用 `YYYY-MM-DD-slug.md`，并在 front matter 中设置
`title`、`date`、`categories`、`tags` 和稳定的 `permalink`。

## 本地预览

```bash
bundle install
bundle exec jekyll serve
```

浏览器打开 `http://localhost:4000`。

生成可直接打开、无需网络连接的预览压缩包：

```bash
bundle exec jekyll build
python3 scripts/make_preview.py _site famatf.com-preview.zip
```
