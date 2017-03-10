''''''
def generate_graph(words):
    from string import ascii_lowercase as lowercase
    G = nx.Graph(name="words")
    lookup = dict((c,lowercase.index(c)) for c in lowercase)
    def edit_distance_one(word):
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i+1:]
            j = lookup[c] # lowercase.index(c)
            for cc in lowercase[j+1:]:
                yield left + cc + right
    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G

def words_graph():
    """Return the words example graph from the Stanford GraphBase"""
    import gzip
    fh=gzip.open('words_dat.txt.gz','r')
    words=set()
    for line in fh.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w=str(line[0:5])
        words.add(w)
    return generate_graph(words)

if __name__ == '__main__':
    from networkx import *
    G=words_graph()
    print("Loaded words_dat.txt containing 5757 five-letter English words.")
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          %(number_of_nodes(G),number_of_edges(G)))
    print("%d connected components" % number_connected_components(G))

    for (source,target) in [('chaos','order'),
                            ('nodes','graph'),
                            ('pound','marks')]:
        print("Shortest path between %s and %s is"%(source,target))
        try:
            sp=shortest_path(G, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")
'''


**Tests:**


**Five Letter Words:**


**i. chaos to order**

    chaos

    chats

    coats

    colts

    colas

    codas

    codes

    coder

    cider

    eider

    elder

    older

    order


**ii. nodes to graph**
    
    nodes
    
    modes
    
    moles
    
    molds
    
    golds
    
    goads
    
    grads
    
    grade
    
    grape
    
    graph


**iii. moron to smart**

    moron

    boron

    baron

    caron

    capon

    capos

    capes

    canes

    banes

    bands

    bends

    beads

    bears

    sears

    stars

    start

    smart


**iv. pound to marks**
    There is no solution.



**Four Letter Words:**


**cold to warm**

cold

cord

word

worm

warm


**love to hate**

love

hove

have

hate



**Variation where two words (nodes) are adjacent if the number of letters that differ:**


**Five Letter Words:**


**i. chaos to order**
   
       chaos

       chose

       chore

       horde

       order


**ii. nodes to graph**
    
    nodes
    
    noses
    
    oases
    
    gases
    
    gasps
    
    grasp
    
    graph


**iii. moron to smart**
   
       moron

       morns

       morts

       marts

       smart


**iv. pound to marks**
     
     pound
     
     ponds
     
     prods
     
     pards
     
     parks
     
     marks


**Four Letter Words:**


**cold to warm**

cold

coal

carl

char

harm

warm


**love to hate**

love

hove

have

hate



**Find words that precede SLID, DOTE, HERD and OMEN and the words that follow NINE, SELL, STAT and WHAT:**


**Words that precede and follow SLID:**

said

slim

sled

slit

slip

skid


**Words that precede and follow DOTE:**

tote

dove

dope

doge

dome

dole

dose

note

vote

done

date

rote

doze


**Words that precede and follow HERD:**

head

hero

herb

hera

hard

here

held

heed

herr

hurd


**Words that precede and follow OMEN:**

oman

oxen

open

oven

amen


**Words that precede and follow NINE:**

dine

vine

mine

nile

nina

tine

pine

none

wine

line

sine

fine

nice

**Words that precede and follow SELL:**

bell

self

nell

well

dell

cell

fell

seal

hell

yell

sill

tell


**Words that precede and follow STAT:**

star

swat

slat

seat

stag

stab

skat

stan

stay

scat

spat

**Words that precede and follow WHAT:**

whit

wham

whet

chat

that


**Project Repository:** https://github.com/shanalily/DeepReader/blob/master/README.md
