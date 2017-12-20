# Maintainer : vmavromatis <8668731+vmavromatis@users.noreply.github.com>
# Contributor : stiefel40k 
pkgname=absolutely-proprietary
pkgver=1
pkgrel=1
pkgdesc="Proprietary package detector for arch-based distros."
arch=('any')
url="https://github.com/vmavromatis/absolutely-proprietary"
license=('GPL3')
depends=('python>=3.6.3')
source=("https://github.com/vmavromatis/absolutely-proprietary/releases/downliad/$pkgver/<to_be_filled_out>")
sha256sums=("<to_be_filled_out>")

package() {
  cd "$srcdir"
  install -Dm755 main.py "$pkgdir/usr/bin/absolutely-proprietary"
}
