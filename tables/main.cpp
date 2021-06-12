#include <iostream>

int main() {
    for (auto x = 0; x <= 1; ++x) {
        for (auto y = 0; y <= 1; ++y) {
            for (auto z = 0; z <= 1; ++z) {
                std::cout << x << " " << y << " " << z << " " << " " << ((not x and y and z) or (not x and not y and z) or (not x and not y and not z)) << '\n';
            }
        }
    }
    return 0;
}
