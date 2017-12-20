# Maintainer : vmavromatis <bill.mavromatis@protonmail.com>
# Contributors : https://github.com/vmavromatis/absolutely-proprietary/graphs/contributors
_pkgname=absolutely-proprietary
pkgname=${_pkgname}-git
pkgver=r54.93d1c3e
pkgrel=1
pkgdesc="Proprietary package detector for arch-based distros."
arch=('any')
url="https://github.com/vmavromatis/${_pkgname}"
license=('GPL3')
depends=('python'
         'python-setuptools')
source=("git+https://github.com/vmavromatis/${_pkgname}.git")
md5sums=('SKIP')

pkgver() {
    cd "${_gitname}"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd "${_gitname}"
  python setup.py install --prefix=/usr --root="$pkgdir/" --optimize=1
  install -Dm644 "$srcdir/${_gitname}/LICENSE.md" \
                 "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
