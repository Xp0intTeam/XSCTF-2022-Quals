src = $(wildcard *.cpp)
target = $(patsubst %.cpp, %, $(src))

CXXFLAGS = -std=c++17 \
	-O3\
	-Wl,-z,relro,-z,now\
	-fstack-protector-strong

.PHONY: all
all: $(target)

$(target): % : %.cpp
	$(CXX) $^ $(CXXFLAGS) -o $@

