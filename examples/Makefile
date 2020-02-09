.PHONEY: all
all:
	{ \
	set -e ;\
	export GRC_HIER_PATH=`pwd`/build ;\
	mkdir -p build/ ;\
	grcc -d build genesis/genesis-g59-xcvr.grc ;\
	grcc -d build genesis/pyqtsdrgui.grc ;\
	}

