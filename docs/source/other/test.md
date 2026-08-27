# 备忘录

## 网站部署相关命令

```bat
cd /d G:\docs_site
rmdir /s /q docs\build
sphinx-build -b html -E -a docs/source docs/build/html
start docs\build\html\index.html
```

```bat
sphinx-autobuild -a -E docs/source docs/build/html
```

```bat
cd /d G:\docs_site
git pull --rebase origin main   # pull到本地
git add .                       # 加入git
git commit -m "update notes"    # 提交
git push                        # push到GitHub
```

```bat
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

## Linux计算命令

```bash
find run -name RUNNING -print | sort
find run -name ENDED -print | sort
```

```bash
for f in $(ls -t run/*/OUTCAR | head -100); do
  if grep -q "Total CPU" "$f"; then
    d=${f%/OUTCAR}
    e=$(grep "Elapsed time" "$f" | awk '{print $4}')
    echo "$d  $e"
  fi
done | head -20
```

```bash
for f in $(ls -t run/*/OUTCAR | head -100); do
  if grep -q "Total CPU" "$f"; then
    grep "Elapsed time" "$f" | awk '{print $4}'
  fi
done | head -20 | awk '{sum+=$1;n++} END{print "n=",n,"avg_sec=",sum/n,"avg_hour=",sum/n/3600}'
```

```bash
for ii in 001; do
  echo "===== $ii ====="
  grep "Elapsed time" run/$ii/OUTCAR
  grep "DAV:" run/$ii/OUTCAR | wc -l
  grep "RMM:" run/$ii/OUTCAR | wc -l
  tail -n 5 run/$ii/OSZICAR
done
```

```
grep "free  energy" OUTCAR | tail
grep "E-fermi" OUTCAR | tail
grep "reached required accuracy" OUTCAR
grep "Voluntary context switches" OUTCAR
```

待补充
