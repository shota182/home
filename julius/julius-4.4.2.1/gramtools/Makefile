# Copyright (c) 1991-2016 Kawahara Lab., Kyoto University
# Copyright (c) 2000-2005 Shikano Lab., Nara Institute of Science and Technology
# Copyright (c) 2005-2016 Julius project team, Nagoya Institute of Technology

# All rights reserved
#
SHELL=/bin/sh
RM=/usr/bin/rm -f
prefix=/usr/local
exec_prefix=${prefix}
INSTALL=/usr/bin/install -c

SUBDIRS=mkdfa dfa_minimize generate accept_check nextword yomi2voca gram2sapixml dfa_determinize 

.PHONY: all install install.bin clean distclean

all install install.bin clean distclean: $(SUBDIRS)

all: TARGET=all

install: TARGET=install

install.bin: TARGET=install.bin

clean: TARGET=clean
clean:
	$(RM) config.log config.cache

distclean: TARGET=distclean
distclean:
	$(RM) config.log config.cache
	$(RM) config.status
	$(RM) Makefile


$(SUBDIRS): force
	@ test -f $@/Makefile && $(MAKE) -C $@ $(TARGET)

.PHONY: force

force :;
