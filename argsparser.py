def parseArgs(args):
    toret = {}
    for arg in args:
        assert '--' in arg
        assert '=' in arg
        argSplit = arg.split('=')
        name = argSplit[0].replace('--', '')
        
        if len(argSplit) == 2:
            toret[name] = argSplit[1]
        else:
            toret[name] = True
    
    return toret

if __name__ == '__main__':
    print(parseArgs(['--test=a']))
    print(parseArgs(['--test=a', '--test2=b']))
    print(parseArgs(['--test=a', '--test2=b', ' --testFlag=']))
    print(parseArgs(['--t='])) 
#OPT  engade funcionalidade de argumentos reducidos
