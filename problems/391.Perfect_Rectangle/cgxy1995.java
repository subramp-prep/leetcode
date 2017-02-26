public boolean isRectangleCover(int[][] rectangles) {
    Set<String> set = new HashSet<>();
    for(int[] rec: rectangles){
        //b = bottom, l = left, r = right, t = top
        //create corners with type
        String bl = rec[0]+","+rec[1]+"bl";
        String br = rec[2]+","+rec[1]+"br";
        String tl = rec[0]+","+rec[3]+"tl";
        String tr = rec[2]+","+rec[3]+"tr";
        //if these corners already exist, return false
        if(!set.add(bl) || !set.add(br) || !set.add(tl) || !set.add(tr)) return false;
        //if these 4 corners and previously added corners form a line, remove them
        if(set.remove(rec[0]+","+rec[1]+"tl")) set.remove(bl);
        else if(set.remove(rec[0]+","+rec[1]+"br")) set.remove(bl);
        if(set.remove(rec[2]+","+rec[1]+"bl")) set.remove(br);
        else if(set.remove(rec[2]+","+rec[1]+"tr")) set.remove(br);
        if(set.remove(rec[0]+","+rec[3]+"tr")) set.remove(tl);
        else if(set.remove(rec[0]+","+rec[3]+"bl")) set.remove(tl);
        if(set.remove(rec[2]+","+rec[3]+"tl")) set.remove(tr);
        else if(set.remove(rec[2]+","+rec[3]+"br")) set.remove(tr);
    }
    //a perfect rectangle contains 4 corners
    return set.size()==4;
}