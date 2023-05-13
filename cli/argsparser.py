def parseArgs(args):
    '''The parser function provided as the skeleton of the project.'''
    toret = {}
    for arg in args:
        assert '--' in arg # changed from the original
        argSplit = arg.split('=')
        name = argSplit[0].replace('--', '')
        
        if len(argSplit) == 2:
            toret[name] = argSplit[1]
        else:
            toret[name] = name # changed from the original
    
    return toret

if __name__ == '__main__':
    print(parseArgs(['--test=a']))
    print(parseArgs(['--test=a', '--test2=b']))
    print(parseArgs(['--test=a', '--test2=b', ' --testFlag=']))
    print(parseArgs(['--rename'])) 
