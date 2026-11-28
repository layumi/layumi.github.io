# The DQ-painter project page arrives as a submodule, and its own repo keeps
# the site under docs/ (that is the folder GitHub Pages publishes for it). It
# has to answer on /DQ-painter/, so copy docs/ one level up after the site is
# written. A copy rather than a move on purpose: if this hook ever stops
# running, the vercel.json rewrite still serves the assets from docs/.
require "fileutils"

Jekyll::Hooks.register :site, :post_write do |site|
  src = File.join(site.source, "DQ-painter", "docs")
  dst = File.join(site.dest, "DQ-painter")

  next unless File.directory?(src)

  FileUtils.mkdir_p(dst)
  Dir.children(src).each do |entry|
    FileUtils.cp_r(File.join(src, entry), dst, preserve: true)
  end
end
