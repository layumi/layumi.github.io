# The DQ-painter project page comes in as a submodule, and its own repo keeps
# the site under docs/ (that is what GitHub Pages publishes for it). It has to
# answer on /DQ-painter/, so flatten docs/ one level up once the site is
# written. Doing it here keeps the URL host-independent: no rewrite rules that
# depend on how a CDN resolves a directory index.
require "fileutils"

Jekyll::Hooks.register :site, :post_write do |site|
  src = File.join(site.dest, "DQ-painter", "docs")
  dst = File.join(site.dest, "DQ-painter")

  next unless File.directory?(src)

  Dir.children(src).each do |entry|
    target = File.join(dst, entry)
    next if File.exist?(target)
    FileUtils.mv(File.join(src, entry), target)
  end

  begin
    Dir.rmdir(src)
  rescue SystemCallError
    # not empty, leave it alone
  end
end
