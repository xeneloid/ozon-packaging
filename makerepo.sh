#!/bin/sh

basedir="../www/repo"
releases=("21" "22")

for rel in ${releases[@]}; do
	repodir="$basedir/$rel"

	# Create repo directory
	mkdir -p $repodir
	mkdir -p $repodir/{SRPMS,noarch,i686,x86_64}

	# Copy files to repo
	[[ -f SRPMS/$rel/*.src.rpm ]] && cp -fu SRPMS/$rel/*.src.rpm $repodir/SRPMS/
	[[ -f RPMS/$rel/*.noarch.rpm ]] && cp -fu RPMS/$rel/*.noarch.rpm $repodir/noarch/
	[[ -f RPMS/$rel/*.i686.rpm ]] && cp -fu RPMS/$rel/*.i686.rpm $repodir/i686/
	[[ -f RPMS/$rel/*.x86_64.rpm ]] && cp -fu RPMS/$rel/*.x86_64.rpm $repodir/x86_64/

	# Create repo data
	createrepo $repodir
done

